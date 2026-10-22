"""assure_step.py <assure-action checkout> <app tree> <out.json> <api url>: run Assure on one app tree as a customer would.

0. Make the tree a git checkout (one commit), which is what `actions/checkout` gives the Action in a workflow; the
   Action reads the repository from the checkout (`git ls-files`).
1. Draft the declaration through the public API (POST /v1/declaration-proposal), the same call the Action makes when a
   repository has no .assure/declaration.json, and write it to <app>/.assure/declaration.json.
2. Run the published Action's step as action.yml does (`python -I -B action/entry.py` in the workspace) in api mode (python-auth-declared-model) on the tree, with your key from
   ASSURE_API_KEY. The verdict envelope is written to <out.json>.

The key is read from the environment only, never from a flag, and it is never printed.
"""
import json, os, subprocess, sys
from pathlib import Path

action, tree, out, api = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), sys.argv[4]
key = os.environ.get('ASSURE_API_KEY', '').strip()
if not key:
    sys.exit('ASSURE_API_KEY is not set')

env = {'PATH': os.environ.get('PATH', ''), 'HOME': os.environ.get('HOME', ''), 'INPUT_MODE': 'api', 'INPUT_API_KEY': key,
       'INPUT_API_URL': api, 'INPUT_PROFILE': 'python-auth-declared-model', 'INPUT_OUTPUT': str(out),
       'INPUT_COMPILE_REQUIREMENTS': 'false', 'GITHUB_WORKSPACE': str(tree), 'RUNNER_TEMP': str(tree.parent),
       'GITHUB_STEP_SUMMARY': str(out.with_suffix('.summary.md')), 'GITHUB_OUTPUT': str(out.with_suffix('.outputs'))}

def git(*args):
    return subprocess.run(['git', '-C', str(tree), *args], env={'PATH': env['PATH'], 'HOME': env['HOME']},
                          capture_output=True, text=True, check=True)

# 0. The Action reads the repository from the checkout itself (`git ls-files` at HEAD; action/repository_manifest.py
#    from_checkout), which in a workflow is the work `actions/checkout` does first. The app tree here is a plain copy,
#    so make it the same kind of checkout: one commit holding exactly the app's files.
if not (tree / '.git').exists():
    git('init', '-q')
    git('add', '-A')
    git('-c', 'user.name=assure-benchmark', '-c', 'user.email=benchmark@invalid', 'commit', '-q', '-m', 'app tree')

# 1. Draft the declaration through the public API, as the Action does for a repository with none, and commit it
#    the way a customer would, so the checkout the Action reads holds it.
if not (tree / '.assure' / 'declaration.json').exists():
    sys.path.insert(0, str(action))
    os.environ.update(env)
    from action import client as C, declaration_draft as DD  # the published Action's own modules
    files = {str(p.relative_to(tree)): p.read_bytes() for p in tree.rglob('*.py') if '.assure' not in p.parts and '.git' not in p.parts}
    rec = DD.draft(files, client=C.Client(api, key))
    (tree / '.assure').mkdir(exist_ok=True)
    decl = rec['declaration']
    # The customer's answer to "which routes are public by design" (APPS.json public_routes), as the setup agent asks it.
    slug = tree.name.rsplit('-', 1)[0]
    apps = {a['slug']: a for a in json.load(open(Path(__file__).resolve().parent / 'APPS.json'))['apps']}
    decl['public_routes'] = apps.get(slug, {}).get('public_routes', [])
    (tree / '.assure' / 'declaration.json').write_text(json.dumps(decl, indent=2, sort_keys=True))
    git('add', '.assure/declaration.json')
    git('-c', 'user.name=assure-benchmark', '-c', 'user.email=benchmark@invalid', 'commit', '-q', '-m', 'declaration')

# 2. Run the published Action's step exactly as action.yml does: `"$ASSURE_PYTHON" -I -B "$GITHUB_ACTION_PATH/action/entry.py"`,
#    with the workspace as the working directory.
r = subprocess.run([sys.executable, '-I', '-B', str(action / 'action' / 'entry.py')], cwd=str(tree), env=env,
                   capture_output=True, text=True)
print('%s: assure exit %d' % (tree.name, r.returncode))
if r.returncode not in (0, 1, 3):
    sys.stderr.write(r.stderr[-2000:])
