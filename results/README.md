# Results

Each release has one folder: `results/<assure-release>/`. It holds:
- `VERSIONS.txt`, the exact tool versions;
- for each app and each tree (clean, planted): the Bandit JSON, the CodeQL SARIF and the Assure verdict envelope;
- `<app>.<rev>.<tool>.items`, every finding on its own line, as `file:line rule`;
- `SUMMARY.md`, made by `score.py`.

**Published run:** `results/v0.1.2/`, made on 22 October 2026 with `run.sh` exactly as it ships here, on Assure v0.1.2 (engine e698723a, Action commit v0.1.2).

Semgrep results are not published here. METHOD.md explains why. You can produce them on your own machine with `WITH_SEMGREP=1 ./run.sh`.
