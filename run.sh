#!/usr/bin/env bash
# Reproduce the Assure benchmark from a clean machine.
#
#   ./run.sh                      Bandit and CodeQL, as published in results/
#   ASSURE_API_KEY=... ./run.sh   ...and Assure, through the public API with your own key
#   WITH_SEMGREP=1 ./run.sh       ...and Semgrep, with its rules fetched on your machine (see METHOD.md)
#
# Needs: git, python3 3.11, 3.12 or 3.13 (Bandit 1.8.6 fails on 3.14: its ast use was removed), curl, unzip. Every tool version is pinned below. Output: out/<app>.<rev>.<tool>.*
# and out/SUMMARY.md. Nothing is uploaded anywhere, except to the Assure API when you set ASSURE_API_KEY.
set -euo pipefail

BANDIT_VERSION=1.8.6
CODEQL_VERSION=2.27.1          # CodeQL bundle v2.27.1, default suite codeql/python-queries (python-code-scanning.qls)
SEMGREP_VERSION=1.181.0
SEMGREP_RULES_COMMIT=a84ff9cc2453ca91d581380de4b8b3f272f6f4be   # python/flask, python/django, python/lang/security
ASSURE_ACTION_REF=${ASSURE_ACTION_REF:-v0.1.0-beta.51}           # the published Action; set to the release you test
ASSURE_API_URL=${ASSURE_API_URL:-https://api.symbolia.ai}

HERE=$(cd "$(dirname "$0")" && pwd); OUT=$HERE/out; W=$HERE/.work
python3 -c 'import sys; sys.exit(0 if (3, 11) <= sys.version_info[:2] <= (3, 13) else 1)' \
  || { echo "python3 must be 3.11 to 3.13: Bandit 1.8.6 raises on every file under 3.14, which would read as zero findings"; exit 2; }
mkdir -p "$OUT" "$W"

# --- tools -------------------------------------------------------------------------------------------------------
python3 -m venv "$W/venv"; "$W/venv/bin/pip" -q install "bandit==$BANDIT_VERSION"
case "$(uname -s)-$(uname -m)" in
  Darwin-*) CQ_PKG=codeql-bundle-osx64.tar.gz ;; Linux-x86_64) CQ_PKG=codeql-bundle-linux64.tar.gz ;;
  *) echo "CodeQL: no bundle for $(uname -s)-$(uname -m)"; exit 2 ;;
esac
if [ ! -x "$W/codeql/codeql" ]; then
  curl -fsSL -o "$W/$CQ_PKG" "https://github.com/github/codeql-action/releases/download/codeql-bundle-v$CODEQL_VERSION/$CQ_PKG"
  tar -xzf "$W/$CQ_PKG" -C "$W"
fi
CQ=$W/codeql/codeql
if [ "${WITH_SEMGREP:-}" = 1 ]; then
  "$W/venv/bin/pip" -q install "semgrep==$SEMGREP_VERSION"
  [ -d "$W/semgrep-rules" ] || git clone -q https://github.com/semgrep/semgrep-rules "$W/semgrep-rules"
  git -C "$W/semgrep-rules" checkout -q "$SEMGREP_RULES_COMMIT"
fi
if [ -n "${ASSURE_API_KEY:-}" ]; then
  [ -d "$W/assure-action" ] || git clone -q https://github.com/Symbolia-Assurance/assure-action "$W/assure-action"
  git -C "$W/assure-action" checkout -q "$ASSURE_ACTION_REF"
fi
{ echo "bandit $BANDIT_VERSION"; echo "codeql $("$CQ" version --format=terse)"; [ "${WITH_SEMGREP:-}" = 1 ] && echo "semgrep $SEMGREP_VERSION rules $SEMGREP_RULES_COMMIT"; [ -n "${ASSURE_API_KEY:-}" ] && echo "assure-action $ASSURE_ACTION_REF api $ASSURE_API_URL"; } > "$OUT/VERSIONS.txt"

# --- apps --------------------------------------------------------------------------------------------------------
apps=$(python3 -c "import json;print(' '.join(a['slug'] for a in json.load(open('$HERE/APPS.json'))['apps']))")
for app in $apps; do
  read -r url commit subdir include < <(python3 - "$HERE/APPS.json" "$app" <<'PY'
import json, sys
a = next(x for x in json.load(open(sys.argv[1]))['apps'] if x['slug'] == sys.argv[2])
url = a['upstream'].split('/tree/')[0]
print(url, a['commit'], a['copy'].get('subdir', '.'), ','.join(a['copy'].get('include', [])) or '-')
PY
)
  src=$W/src/$app; [ -d "$src" ] || { git init -q "$src"; git -C "$src" fetch -q --depth 1 "$url" "$commit"; git -C "$src" checkout -q FETCH_HEAD; }
  for rev in clean head; do
    d=$W/tree/$app-$rev; rm -rf "$d"; mkdir -p "$d"
    if [ "$include" = - ]; then cp -R "$src/$subdir/." "$d/"; else for f in ${include//,/ }; do cp "$src/$f" "$d/"; done; fi
    rm -rf "$d/.git"
    if [ $rev = head ]; then (cd "$d" && git init -q && git apply --unidiff-zero "$HERE/plants/$app.patch"); rm -rf "$d/.git"; fi
    "$W/venv/bin/bandit" -q -r "$d" -f json -o "$OUT/$app.$rev.bandit.json" || true
    "$CQ" database create "$W/db-$app-$rev" --language=python --source-root="$d" --overwrite >/dev/null
    "$CQ" database analyze "$W/db-$app-$rev" codeql/python-queries --format=sarif-latest --output="$OUT/$app.$rev.codeql.sarif" >/dev/null
    if [ "${WITH_SEMGREP:-}" = 1 ]; then
      "$W/venv/bin/semgrep" scan --metrics=off --disable-version-check --quiet --json -o "$OUT/$app.$rev.semgrep.json" \
        --config "$W/semgrep-rules/python/flask" --config "$W/semgrep-rules/python/django" --config "$W/semgrep-rules/python/lang/security" "$d" || true
    fi
    if [ -n "${ASSURE_API_KEY:-}" ]; then
      python3 "$HERE/assure_step.py" "$W/assure-action" "$d" "$OUT/$app.$rev.assure.json" "$ASSURE_API_URL"
    fi
  done
done
python3 "$HERE/score.py" "$OUT" "$HERE/APPS.json" > "$OUT/SUMMARY.md"
cat "$OUT/SUMMARY.md"
