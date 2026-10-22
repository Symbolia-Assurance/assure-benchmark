The proof tree for this run is on Assure Premium, which also checks your app&#x27;s sign-in and session model in depth: a formal model of your app&#x27;s sign-in. Upgrade for USD 20 a month to see it: <<upgrade-url-removed>>

## This change breaks 1 rule.

The job stops (exit 1).

### What to do next

1. Fix each broken rule below: each one names the line and the fix, then run Assure again.
2. Read "Not checked yet" below: each rule there says why Assure could not decide it yet.

### Broken: Every private route needs sign-in (AUTH-1)

What this change does: lets anyone reach GET /export without signing in.; premised: stated by you (instance\_config = &quot;constants-only&quot;). Where: `flaskr/blog.py:128`.

**Fix:** Add the sign-in guard to the view for GET /export (and the admin guard if it is an admin route), as the other protected views have.

### Not checked yet

- **Role-guarded routes admit only that role:** the check could not look at this part; your agent can propose coverage; premised: stated by you (instance\_config = &quot;constants-only&quot;).
- **Sign-in needs the second-factor code:** the check could not look at this part; your agent can propose coverage; premised: stated by you (instance\_config = &quot;constants-only&quot;).
- **Signing out always signs you out:** the check could not look at this part; your agent can propose coverage; premised: stated by you (instance\_config = &quot;constants-only&quot;).
- **Step-up sign-in starts only from a signed-in admin:** the check could not look at this part; your agent can propose coverage; premised: stated by you (instance\_config = &quot;constants-only&quot;).


<details><summary>Details for agents: every reading with its status, reason and obligation id, and the exit</summary>

**Assure: red: 1 of 1 machines read; declared premises: 5; version pins: none; disproven: AUTH-1 — flaskr/blog.py:128**

Anyone who can reach your Flask app can call a route outside your declared public routes without signing in. The finding is at flaskr/blog.py:128.

Usable readings: 1 of 6. Coverage complete: yes. Job stops: yes (exit 1).

### Unsupported by this profile version: 5

- AUTH-2: the input could not be represented — agent: a faithful input: the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-2 is not established; next step: confirm that
- AUTH-3: the input could not be represented — agent: a faithful input: the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-3 is not established; next step: confirm that
- AUTH-4: the input could not be represented — agent: a faithful input: the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-4 is not established; next step: confirm that
- AUTH-5: the input could not be represented — agent: a faithful input: the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-5 is not established; next step: confirm that
- AUTH-6: no method for this shape — symbolia: a method for this input shape

### Why it matters

- AUTH-1: No route outside the declared public routes is reachable without signing in. Anyone who can reach your Flask app can call a route outside your declared public routes without signing in.

Profile python-auth-declared-model, check 159c84c3ba418f8ffdc2558892409a43.
Policy: the job stops with exit 1 when any reading is fails.
This run: exit 1, because a reading has a status the policy fails on.

| Status | Count |
| --- | --- |
| fails | 1 |
| representation | 4 |
| missing method | 1 |
| not evaluated | 0 |
| holds | 0 |

### fails

- M1 AUTH-1: fails; premised: stated by you (instance\_config = &quot;constants-only&quot;) (enabled from ANON with no effective guard: GET /export (no effective guard on the view))

### representation

- M1 AUTH-2: not established (missing\_premise); premised: stated by you (instance\_config = &quot;constants-only&quot;) (the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-2 is not established; next step: confirm that click registers no route, writes no session key and installs no pre-view hook in your app, then re…)
- M1 AUTH-3: not established (missing\_premise); premised: stated by you (instance\_config = &quot;constants-only&quot;) (the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-3 is not established; next step: confirm that click registers no route, writes no session key and installs no pre-view hook in your app, then re…)
- M1 AUTH-4: not established (missing\_premise); premised: stated by you (instance\_config = &quot;constants-only&quot;) (the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-4 is not established; next step: confirm that click registers no route, writes no session key and installs no pre-view hook in your app, then re…)
- M1 AUTH-5: not established (missing\_premise); premised: stated by you (instance\_config = &quot;constants-only&quot;) (the premise that click registers no route, writes no session key and installs no pre-view hook is Assure&#x27;s drafted proposal, not confirmed by you, so AUTH-5 is not established; next step: confirm that click registers no route, writes no session key and installs no pre-view hook in your app, then re…)

### missing method

- M1 AUTH-6: not established (missing\_method); premised: stated by you (instance\_config = &quot;constants-only&quot;) (not established, gap auth6-bearer-token-v1: Bearer-token checking is not established in v1: the declared idiom is session-based.)

### Scope

- A reading states what the submitted repository satisfies under the declared model over AUTH-CATALOGUE-001: the routes registered in source, their guards and the session keys the declaration names. It runs no code of yours, contacts no server, and certifies no deployment.
- An obligation no method states is not established until a method states it; a reading the repository&#x27;s shape does not admit is not established, and the summary says why, naming in plain words the line Assure could not read when the checker names one.
- The route set is the (method, path) pairs registered in source. Framework responses that run no view and error-handler bodies are outside the model.
- The route set is the (method, path) pairs registered in source. A route registered for GET also answers HEAD with the same view, and its method tests are read for both. Framework responses that run no view (automatic OPTIONS and the static route) are outside the model, and so are error-handler bodi…

Add coverage: Assure does not cover Role-guarded routes admit only that role, Sign-in needs the second-factor code, Signing out always signs you out and Step-up sign-in starts only from a signed-in admin here yet. Your agent can propose the coverage with POST /v1/coverage/proposals, following skills/assure/references/coverage.md; it asks you before it sends anything, and nothing it sends runs.

</details>

The report was withheld: this report is quoted at USD 0.13 and USD 0.00 is left of the free report balance, which does not renew, so it does not run; a paid plan gives more reports.

### Withheld in the runner

Withheld in the runner before anything was sent: nothing to withhold — the withholding pass covers PostgreSQL configuration and pg_hba files and the SQL literals in the catalog snapshot and the declaration, and this profile's inputs name none of them.
