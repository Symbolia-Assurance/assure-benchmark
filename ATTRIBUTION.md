# Attribution

This repository fetches each app from its upstream at the pinned commit. It contains no app source except the plant patches in `plants/`, which are small changes to that source. Each patch is distributed under its app's licence, with its copyright notice kept here.

| App | Upstream | Commit | Licence | Copyright |
|---|---|---|---|---|
| microblog | https://github.com/miguelgrinberg/microblog | `a975ef648643` | MIT | Miguel Grinberg (2017) |
| flasky | https://github.com/miguelgrinberg/flasky | `3beedd640b91` | MIT | Miguel Grinberg (2013) |
| flask-base | https://github.com/hack4impact/flask-base | `811fda1cb350` | MIT | Hack4Impact (2018) |
| realworld | https://github.com/gothinkster/flask-realworld-example-app | `4b95fb2227df` | MIT | Mohamed Aziz Knani (2017) |
| flask-user-starter | https://github.com/lingthio/Flask-User-starter-app | `9d97fc2b7236` | BSD-2-Clause | Ling Thio and contributors (2013) |
| cookiecutter-demo | https://github.com/jamescurtin/demo-cookiecutter-flask | `afae7e9c7d89` | MIT | jamescurtin, demo-cookiecutter-flask (2025) |
| jwt-restful | https://github.com/oleg-agapov/flask-jwt-auth | `d68bb2522f9d` | MIT | oleg-agapov (2017) |
| rest-tutorial | https://github.com/miguelgrinberg/REST-tutorial | `eefcd127cf41` | MIT | Miguel Grinberg (2013) |
| flaskr | https://github.com/pallets/flask/tree/main/examples/tutorial | `d086db856be1` | BSD-3-Clause | Pallets (2010) |
| flask-bones | https://github.com/cburmeister/flask-bones | `bc61f5c12b50` | MIT | Corey Burmeister (2017) |

Full licence texts are in each upstream repository at the pinned commit. Bandit (Apache-2.0) and CodeQL (GitHub CodeQL Terms and Conditions) are downloaded by `run.sh` and not redistributed here. Semgrep and its rules are fetched only when you set `WITH_SEMGREP=1`; see METHOD.md.
