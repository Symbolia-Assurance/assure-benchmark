The proof tree for this run is on Assure Premium, which also checks your app&#x27;s sign-in and session model in depth: a formal model of your app&#x27;s sign-in. Upgrade for USD 20 a month to see it: <<upgrade-url-removed>>

## Assure could not read before\_app\_request at app/auth/views.py:12, so it checked nothing in this change.

The job stops (exit 3).

### What to do next

1. Look at the line named above: Assure does not read it yet. Rewrite it in a form Assure reads, or tell Symbolia it needs reading, then run Assure again.

### Environment assumptions from source

- Config.FLASKY\_ADMIN: env variable name FLASKY\_ADMIN; environment not read; runtime value unknown; no default; source config.py:15
- Config.MAIL\_PASSWORD: env variable name MAIL\_PASSWORD; environment not read; runtime value unknown; no default; source config.py:12
- Config.MAIL\_PORT: env variable name MAIL\_PORT; environment not read; runtime value unknown; source default &quot;587&quot;; absent only; int conversion; conditional default 587; invalid present input is not a fallback; source config.py:8
- Config.MAIL\_SERVER: env variable name MAIL\_SERVER; environment not read; runtime value unknown; source default &quot;smtp.googlemail.com&quot;; absent only; source config.py:7
- Config.MAIL\_USERNAME: env variable name MAIL\_USERNAME; environment not read; runtime value unknown; no default; source config.py:11
- Config.MAIL\_USE\_TLS: env variable name MAIL\_USE\_TLS; environment not read; runtime value unknown; source default &quot;true&quot;; absent only; source config.py:9
- Config.SECRET\_KEY: env variable name SECRET\_KEY; environment not read; runtime value unknown; source default &quot;hard to guess string&quot;; absent or empty; source config.py:6
- DevelopmentConfig.SQLALCHEMY\_DATABASE\_URI: env variable name DEV\_DATABASE\_URL; environment not read; runtime value unknown; source default expression &#x27;`sqlite:///`&#x27; + os.path.join(basedir, &#x27;data-dev.sqlite&#x27;); absent or empty; source config.py:31
- HerokuConfig.SSL\_REDIRECT: env variable name DYNO; environment not read; runtime value unknown; no default; source config.py:72
- ProductionConfig.SERVER\_NAME: env variable name SERVER\_NAME; environment not read; runtime value unknown; no default; source config.py:45
- ProductionConfig.SQLALCHEMY\_DATABASE\_URI: env variable name DATABASE\_URL; environment not read; runtime value unknown; source default expression &#x27;`sqlite:///`&#x27; + os.path.join(basedir, &#x27;data.sqlite&#x27;); absent or empty; source config.py:43
- TestingConfig.SQLALCHEMY\_DATABASE\_URI: env variable name TEST\_DATABASE\_URL; environment not read; runtime value unknown; source default &quot;`sqlite://`&quot;; absent or empty; source config.py:37


<details><summary>Details for agents: every reading with its status, reason and obligation id, and the exit</summary>

**Assure: yellow: could not look: the input could not be represented; Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet); review that line in the repository or the declaration and resubmit**

We could not read the submitted input, so nothing below is a finding about your system. Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet); review that line in the repository or the declaration and resubmit.

### Environment assumptions from source

- Config.FLASKY\_ADMIN: env variable name FLASKY\_ADMIN; environment not read; runtime value unknown; no default; source config.py:15
- Config.MAIL\_PASSWORD: env variable name MAIL\_PASSWORD; environment not read; runtime value unknown; no default; source config.py:12
- Config.MAIL\_PORT: env variable name MAIL\_PORT; environment not read; runtime value unknown; source default &quot;587&quot;; absent only; int conversion; conditional default 587; invalid present input is not a fallback; source config.py:8
- Config.MAIL\_SERVER: env variable name MAIL\_SERVER; environment not read; runtime value unknown; source default &quot;smtp.googlemail.com&quot;; absent only; source config.py:7
- Config.MAIL\_USERNAME: env variable name MAIL\_USERNAME; environment not read; runtime value unknown; no default; source config.py:11
- Config.MAIL\_USE\_TLS: env variable name MAIL\_USE\_TLS; environment not read; runtime value unknown; source default &quot;true&quot;; absent only; source config.py:9
- Config.SECRET\_KEY: env variable name SECRET\_KEY; environment not read; runtime value unknown; source default &quot;hard to guess string&quot;; absent or empty; source config.py:6
- DevelopmentConfig.SQLALCHEMY\_DATABASE\_URI: env variable name DEV\_DATABASE\_URL; environment not read; runtime value unknown; source default expression &#x27;`sqlite:///`&#x27; + os.path.join(basedir, &#x27;data-dev.sqlite&#x27;); absent or empty; source config.py:31
- HerokuConfig.SSL\_REDIRECT: env variable name DYNO; environment not read; runtime value unknown; no default; source config.py:72
- ProductionConfig.SERVER\_NAME: env variable name SERVER\_NAME; environment not read; runtime value unknown; no default; source config.py:45
- ProductionConfig.SQLALCHEMY\_DATABASE\_URI: env variable name DATABASE\_URL; environment not read; runtime value unknown; source default expression &#x27;`sqlite:///`&#x27; + os.path.join(basedir, &#x27;data.sqlite&#x27;); absent or empty; source config.py:43
- TestingConfig.SQLALCHEMY\_DATABASE\_URI: env variable name TEST\_DATABASE\_URL; environment not read; runtime value unknown; source default &quot;`sqlite://`&quot;; absent or empty; source config.py:37

Usable readings: 0 of 6. Coverage complete: no. Job stops: yes (exit 3).

### Unsupported by this profile version: 6

- Next step for 6 obligations: the input could not be represented — agent: a faithful input: Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet)
  - AUTH-1, AUTH-2, AUTH-3, AUTH-4, AUTH-5, AUTH-6

Profile python-auth-declared-model, check d2d48cfa81cb1dbeb969ddb8339fec2a.

No verdicts: None of the readings is a verdict that checked something; a vacuous reading only says a domain was empty. Read each status below for what was and was not checked.
Policy: the job stops with exit 1 when any reading is fails.
Could not look: nothing could be read, so the job stops with exit 3.

| Status | Count |
| --- | --- |
| fails | 0 |
| representation | 6 |
| missing method | 0 |
| not evaluated | 0 |
| holds | 0 |

Machines refused: 1 (not evaluated 1). A refused machine is not an obligation reading and is not in the table above.

### representation

- M1 AUTH-1: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))
- M1 AUTH-2: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))
- M1 AUTH-3: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))
- M1 AUTH-4: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))
- M1 AUTH-5: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))
- M1 AUTH-6: not established (representation) (Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet))

### Machines not read

- M1: the checker refused the machine: Assure could not read `before_app_request` at `app/auth/views.py:12` (a route registration Assure does not read yet)

### Scope

- A reading states what the submitted repository satisfies under the declared model over AUTH-CATALOGUE-001: the routes registered in source, their guards and the session keys the declaration names. It runs no code of yours, contacts no server, and certifies no deployment.
- An obligation no method states is not established until a method states it; a reading the repository&#x27;s shape does not admit is not established, and the summary says why, naming in plain words the line Assure could not read when the checker names one.
- The route set is the (method, path) pairs registered in source. Framework responses that run no view and error-handler bodies are outside the model.
- The route set is the (method, path) pairs registered in source. A route registered for GET also answers HEAD with the same view, and its method tests are read for both. Framework responses that run no view (automatic OPTIONS and the static route) are outside the model, and so are error-handler bodi…

</details>

The report was withheld: this report is quoted at USD 0.12 and USD 0.00 is left of the free report balance, which does not renew, so it does not run; a paid plan gives more reports.

### Withheld in the runner

Withheld in the runner before anything was sent: nothing to withhold — the withholding pass covers PostgreSQL configuration and pg_hba files and the SQL literals in the catalog snapshot and the declaration, and this profile's inputs name none of them.
