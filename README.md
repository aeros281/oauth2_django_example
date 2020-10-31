# Example using Django Rest Framework to work with existing OAuth 2.0 authentication backends.
Notes: the current implementation only work with AWS Cognito.
# How to run
Create basic database structure (default to work with SQLite):
```bash
  $ python manage migrate
```
Create .env file (should be auto ignored by git) based from .env.example:
```bash
$ cp fun_quiz/.env.example fun_quiz/.env
```
Update .env with correct environment (including Cognito region, pool ID, client id, etc.)

Run server
```bash
  $ ENV_PATH=.env python manage.py runserver
```
# Limitations
- Only support Cognito for now.
- Using Cognito, the client must send `idToken` instead of `accessToken`.
