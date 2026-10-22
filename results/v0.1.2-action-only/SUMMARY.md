# Assure benchmark: ten real Flask apps, one planted unguarded route each

bandit 1.8.6
codeql 2.27.1
assure-action v0.1.2 api https://api.symbolia.ai

| App | Tool | Caught the plant | Findings on clean | Findings on planted |
|---|---|---|---|---|
| microblog | bandit | no | 11 | 11 |
| microblog | codeql | no | 5 | 5 |
| microblog | assure | no | 0 | 0 |
| flasky | bandit | no | 42 | 42 |
| flasky | codeql | no | 1 | 1 |
| flasky | assure | no | 0 | 0 |
| flask-base | bandit | no | 28 | 28 |
| flask-base | codeql | no | 1 | 1 |
| flask-base | assure | no | 0 | 0 |
| realworld | bandit | no | 67 | 67 |
| realworld | codeql | no | 0 | 0 |
| realworld | assure | no | 0 | 0 |
| flask-user-starter | bandit | no | 13 | 13 |
| flask-user-starter | codeql | no | 0 | 0 |
| flask-user-starter | assure | no | 0 | 0 |
| cookiecutter-demo | bandit | no | 63 | 63 |
| cookiecutter-demo | codeql | no | 1 | 1 |
| cookiecutter-demo | assure | no | 0 | 0 |
| jwt-restful | bandit | no | 2 | 2 |
| jwt-restful | codeql | no | 0 | 0 |
| jwt-restful | assure | no | 0 | 0 |
| rest-tutorial | bandit | no | 2 | 2 |
| rest-tutorial | codeql | no | 2 | 2 |
| rest-tutorial | assure | no | 0 | 0 |
| flaskr | bandit | no | 37 | 37 |
| flaskr | codeql | no | 0 | 0 |
| flaskr | assure | yes | 0 | 1 |
| flask-bones | bandit | no | 10 | 10 |
| flask-bones | codeql | no | 1 | 1 |
| flask-bones | assure | no | 0 | 0 |

| Tool | Apps run | Plants caught | Findings on clean (total) | Findings on planted (total) |
|---|---|---|---|---|
| bandit | 10 | 0 of 10 | 275 | 275 |
| codeql | 10 | 0 of 10 | 11 | 11 |
| assure | 10 | 1 of 10 | 0 | 1 |
