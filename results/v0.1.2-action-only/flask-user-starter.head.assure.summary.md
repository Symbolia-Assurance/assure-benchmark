The proof tree for this run is on Assure Premium, which also checks your app&#x27;s sign-in and session model in depth: a formal model of your app&#x27;s sign-in. Upgrade for USD 20 a month to see it: <<upgrade-url-removed>>

## Assure could not read app/\_\_init\_\_.py:37 and other lines, so it checked nothing in this change.

The job stops (exit 3).

### What to do next

1. Look at the line named above: Assure does not read it yet. Rewrite it in a form Assure reads, or tell Symbolia it needs reading, then run Assure again.


<details><summary>Details for agents: every reading with its status, reason and obligation id, and the exit</summary>

**Assure: yellow: could not look: the input could not be represented; Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines; review those lines in the repository or the declaration and resubmit**

We could not read the submitted input, so nothing below is a finding about your system. Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure ca….

Usable readings: 0 of 6. Coverage complete: no. Job stops: yes (exit 3).

### Unsupported by this profile version: 6

- Next step for 6 obligations: the input could not be represented — agent: a faithful input: Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …)
  - AUTH-1, AUTH-2, AUTH-3, AUTH-4, AUTH-5, AUTH-6

Profile python-auth-declared-model, check 3c38e51c37fa421e44c5f19071275aa1.

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

- M1 AUTH-1: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)
- M1 AUTH-2: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)
- M1 AUTH-3: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)
- M1 AUTH-4: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)
- M1 AUTH-5: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)
- M1 AUTH-6: not established (representation) (Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-User&#x27;s UserManager adds routes (/user/sign-in and others) that Assure does not model yet), and other lines)

### Machines not read

- M1: the checker refused the machine: Assure could not read a line at `app/__init__.py:37` (an app object passed where Assure cannot follow it: db is handed to Flask-User&#x27;s UserManager (line 68), which adds routes (/user/sign-in and others) that Assure does not …) and a line at `app/__init__.py:68` (an app object passed where Assure cannot follow it: Flask-U)

### Scope

- A reading states what the submitted repository satisfies under the declared model over AUTH-CATALOGUE-001: the routes registered in source, their guards and the session keys the declaration names. It runs no code of yours, contacts no server, and certifies no deployment.
- An obligation no method states is not established until a method states it; a reading the repository&#x27;s shape does not admit is not established, and the summary says why, naming in plain words the line Assure could not read when the checker names one.
- The route set is the (method, path) pairs registered in source. Framework responses that run no view and error-handler bodies are outside the model.
- The route set is the (method, path) pairs registered in source. A route registered for GET also answers HEAD with the same view, and its method tests are read for both. Framework responses that run no view (automatic OPTIONS and the static route) are outside the model, and so are error-handler bodi…
- guards is not declared (declaration.json#/guards): AUTH-1, AUTH-2, AUTH-3, AUTH-4, AUTH-5, AUTH-6 read not established

</details>

The report was withheld: this report is quoted at USD 0.13 and USD 0.00 is left of the free report balance, which does not renew, so it does not run; a paid plan gives more reports.

### Withheld in the runner

Withheld in the runner before anything was sent: nothing to withhold — the withholding pass covers PostgreSQL configuration and pg_hba files and the SQL literals in the catalog snapshot and the declaration, and this profile's inputs name none of them.
