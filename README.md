# Assure benchmark

Ten real Flask apps with sign-in. Each gets one planted change: a new route that returns data with no sign-in check. This repository shows which tools catch it, and how much each one reports on the original apps.

| Tool | Plants caught | Findings on the original apps |
|---|---|---|
| Bandit 1.8.6 | 0 of 10 | 275 |
| CodeQL 2.27.1 | 0 of 10 | 11 |
| Assure v0.1.2, Skill setup, then the Action | 5 of 10 | 0 |
| Assure v0.1.2, the Action without the setup step | 1 of 10 | 0 |

Run on 22 October 2026: Assure v0.1.2 (engine e698723a), Assure Action v0.1.2 (commit 0edf4191). Every file is in `results/v0.1.2/` and `results/v0.1.2-action-only/`.

Run it yourself with `./run.sh`. Every tool version is pinned. Each finding is listed one by one under `results/`, and METHOD.md explains what is measured, what each tool targets and where Assure does not win.

- Apps, commits and licences: `APPS.json` and `ATTRIBUTION.md`
- Planted changes: `plants/`
- Assure: https://symbolia.ai (free tier: one command for your agent)
