# Method

## The question

A developer adds a new route to a Flask app that has sign-in. The route returns data, and it has no sign-in check, while the app's other data routes do. Does the tool tell them?

That is the one thing this benchmark measures. It is a narrow question, and we chose it on purpose. Missing a check on a new route is a common way for private data to leak, and only a tool that understands how the app decides who is signed in can see it.

## The apps

These are ten public Flask apps with sign-in, each with a permissive licence (MIT, BSD-2-Clause or BSD-3-Clause). Each is pinned at an exact upstream commit. `APPS.json` gives the URL, commit, licence and plant for each one, and `ATTRIBUTION.md` keeps each copyright notice.

They are the apps we used to qualify Assure's free tier before launch. Publishing them means we no longer use them to qualify releases. From now on, releases are qualified on a separate private set built the same way.

For each app the benchmark runs every tool twice:
- **clean:** the upstream app as published;
- **planted:** the upstream app plus `plants/<app>.patch`, one new route with no sign-in check (for example microblog's `/export_all_posts`).

## The scoring rule

- **Caught.** A tool catches the plant when one of its findings on the planted tree lands on a line the patch added. A finding anywhere else does not count as a catch.
- **Findings on clean.** We count every finding on the unchanged upstream app. These apps are not flawless, so some of these findings may be real. We list them all, item by item, in `results/<release>/<app>.clean.<tool>.items`, so you can judge each one yourself.
- **Assure.** A finding is a rule it reports broken (disproven), with a file and line. When Assure cannot read an app well enough to decide, it says "not checked" and names the reason. That counts as no finding, neither a catch nor a false alarm. The results list those reasons per app.

## The tools, and what each one targets

| Tool | Version | Rules | What it looks for |
|---|---|---|---|
| Bandit | 1.8.6 | its built-in tests | Insecure calls and patterns in Python: shell injection, weak hashing, debug mode and the like |
| CodeQL | 2.27.1 | the default `codeql/python-queries` suite (python-code-scanning) | Data-flow vulnerabilities: injection, path traversal, unsafe deserialisation and the like |
| Semgrep | 1.181.0 | semgrep-rules at a84ff9cc: python/flask, python/django, python/lang/security | Pattern rules for framework misuse and insecure code |
| Assure | the release named in each results folder | its own, from the app's declared sign-in model | Whether every route that should require sign-in does, among other promises |

**Read this before quoting a result.** Bandit, CodeQL and Semgrep are not designed to find a missing sign-in check on one route. They look for other classes of flaw, and they are good at those. This benchmark says nothing about how well they find those classes. It measures one thing: whether a tool catches this particular mistake, and how much it reports on code that never had it.

## Where Assure does not win

- **Assure does not read every app.** When it can't prove how an app decides who is signed in, it says "not checked" and names why, rather than guessing. For example, some apps change Flask-Login's anonymous-user class, or turn on an extension from an environment variable. The results show which apps Assure read and which it didn't.
- **Assure checks a narrower set of things than these tools.** It does not look for the injection and insecure-call classes Bandit, CodeQL and Semgrep target. It complements them; it doesn't replace them.

## Why Semgrep's numbers are not published here

`run.sh` can run Semgrep on your machine (`WITH_SEMGREP=1`), fetching its rules there. This repository carries no Semgrep rules and publishes no Semgrep numbers.

The reason is the Semgrep Rules License v1.0 (https://semgrep.dev/legal/rules-license). It says: "You may use the rules only for your own internal business purposes." It also says: "This license does not allow you to distribute the rules, or to make them available to others as a service." Publishing results from those rules is not clearly an internal business purpose, so we leave that step to you, under your own licence.

## Reproduce it

Run `./run.sh`. Every version is pinned in the script. Set `ASSURE_API_KEY` to include Assure: it runs through the public API with your own key, the same way the GitHub Action does. The free tier covers this run.
