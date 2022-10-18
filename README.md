# Vaccination Inventory Backend Dev Test

### Copy .example.env to .env

# Run With Docker

### Start the project

Configure your .env as the example and run `docker-compose up`

### Execute tests

After build, run tests `docker-compose run --rm test`

# Run locally

### Create a locally database in postgres

### Install python 3

### Install requirements

`pip install -r requirements.txt`

### Collect statics (Important for drf-yasg docs)

`python manage.py collectstatic --no-input`

### Migrate

`python manage.py migrate`

### Execute tests

`pytest`

### Run

`python manage.py runserver`

### Install initial fixtures

`python manage.py loaddata fixture_initial_data.json`

# DOCS

### Swagger

[Docs: localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)

### To Authorize in Swagger

In the auth tag go to the auth/ endpoint and enter your username and password. You will get a token in the response, and
you should add it in the following format "Token XXX" (where XXX is the token you just got) to the value of the
authorize section.

# How did I do it?

- First, defined the models and validators.
- I tested the business models.
- Defined the groups and generated the initial fixtures as administrator user and groups per user.
- Defined the serializers for the different use cases with their respective validations.
- Defined the interfaces and default implementations of the services.
- I defined the permissions per role for the api views.
- Defined the api views.
- Finally, I added and described the self-documentation with swagger.
