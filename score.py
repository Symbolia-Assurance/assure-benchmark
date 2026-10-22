"""score.py <out dir> <APPS.json>: score run.sh's outputs.

A tool CATCHES the plant when one of its findings on the planted tree lies in a file the plant patch touches, on a line
the plant added. FINDINGS ON CLEAN counts every finding on the unchanged upstream app. Each finding is itemised in
<out>/<app>.<rev>.<tool>.items. For Assure, a finding is a rule it reports broken (disproven) with a file:line; a run that
reports nothing broken has no findings, whatever else it says."""
import json, re, sys
from pathlib import Path

out, apps_file = Path(sys.argv[1]), Path(sys.argv[2])
HERE = apps_file.parent
APPS = [a['slug'] for a in json.loads(apps_file.read_text())['apps']]
TOOLS = ('bandit', 'codeql', 'semgrep', 'assure')


def plant_lines(app):
    lines, cur = {}, None
    for l in (HERE / 'plants' / f'{app}.patch').read_text().splitlines():
        if l.startswith('+++ b/'):
            cur = l[6:]
        m = re.match(r'@@ -\S+ \+(\d+)(?:,(\d+))? @@', l)
        if m and cur:
            a, n = int(m.group(1)), int(m.group(2) or 1)
            lines.setdefault(cur, set()).update(range(a, a + n))
    return lines


def rel(path, app, rev):
    p = str(path)
    key = f'{app}-{rev}/'
    return p.split(key, 1)[1] if key in p else p.lstrip('./')


def findings(app, rev, tool):
    ext = '.sarif' if tool == 'codeql' else '.json'
    f = out / f'{app}.{rev}.{tool}{ext}'
    if not f.exists():
        return None
    try:
        d = json.loads(f.read_text())
    except Exception:
        return None
    if tool == 'bandit':
        return [(rel(r['filename'], app, rev), r['line_number'], r.get('test_id', '')) for r in d.get('results', [])]
    if tool == 'semgrep':
        return [(rel(r['path'], app, rev), r['start']['line'], r.get('check_id', '').split('.')[-1]) for r in d.get('results', [])]
    if tool == 'codeql':
        res = []
        for run in d.get('runs', []):
            for r in run.get('results', []):
                for loc in r.get('locations', [])[:1]:
                    pl = loc.get('physicalLocation', {})
                    res.append((pl.get('artifactLocation', {}).get('uri', ''), pl.get('region', {}).get('startLine', 0), r.get('ruleId', '')))
        return res
    # assure: each disproven requirement with its locator "path:line". The envelope counts them (counts.fails); the
    # locator is printed in the job summary the Action writes beside it (<app>.<rev>.assure.summary.md), as
    # "disproven: AUTH-1 — path:line".
    res = []
    summ = out / f'{app}.{rev}.assure.summary.md'
    text = json.dumps(d) + (summ.read_text() if summ.exists() else '')
    # Every site of a failing obligation: readings.<machine>.obligations[] whose result_type is "fails" (state disproven), each witness's
    # locator "path:line". (The job summary prints only the first site.)
    for m in (d.get('readings') or {}).values():
        for o in (m.get('obligations') or []) if isinstance(m, dict) else []:
            if o.get('result_type') != 'fails' and o.get('state') != 'disproven':
                continue
            for w in o.get('witnesses') or []:
                mm = re.match(r'^([\w./-]+):(\d+)$', str(w.get('locator') or ''))
                if mm and (mm.group(1), int(mm.group(2)), o.get('id', '')) not in res:
                    res.append((mm.group(1), int(mm.group(2)), o.get('id', '')))
    return res


print('# Assure benchmark: ten real Flask apps, one planted unguarded route each\n')
v = out / 'VERSIONS.txt'
print(v.read_text() if v.exists() else '')
print('| App | Tool | Caught the plant | Findings on clean | Findings on planted |')
print('|---|---|---|---|---|')
tot = {}
for app in APPS:
    pl = plant_lines(app)
    for tool in TOOLS:
        h, c = findings(app, 'head', tool), findings(app, 'clean', tool)
        if h is None:
            continue
        caught = any(f in pl and ln in pl[f] for f, ln, _ in h)
        for rev, items in (('clean', c), ('head', h)):
            (out / f'{app}.{rev}.{tool}.items').write_text(''.join(f'{f}:{ln} {rid}\n' for f, ln, rid in sorted(items or [])))
        t = tot.setdefault(tool, [0, 0, 0, 0])
        t[0] += caught; t[1] += len(c or []); t[2] += len(h); t[3] += 1
        print(f'| {app} | {tool} | {"yes" if caught else "no"} | {len(c or [])} | {len(h)} |')
print('\n| Tool | Apps run | Plants caught | Findings on clean (total) | Findings on planted (total) |')
print('|---|---|---|---|---|')
for tool, (k, c, h, n) in tot.items():
    print(f'| {tool} | {n} | {k} of {n} | {c} | {h} |')
