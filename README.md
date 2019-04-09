# djangorestframework-recipe

A showcase djangorestframework api for creating and finding recipes.

[![Build Status](https://travis-ci.org/jonwhittlestone/djangorestframework-recipe.svg?branch=master)](https://travis-ci.org/jonwhittlestone/djangorestframework-recipe)

---

## Database visualised

The recipe table is central to the app and when finished, should look like this ERD

![ERD](assets/core_recipe_erd.png)

---

## Tests

As per the CI config:

`# you may need to build containers`

`# docker-compose build`

`docker-compose run app sh -c "python manage.py test && flake8"`

---

## Commit Steps

1. Simple docker install. Python container with Django and DRF

   To invoke, run `docker build .`

2. Create docker-compose app service and created an empty django app

   `docker-compose run app sh -c "django-admin.py startproject app."`

3. Add flake8 and Travis-CI configuration

4. Create `core` app with separate tests directory

5. Configure Custom User Model to use email not username (plus some tests)

6. Setting up Django Admin. Test-Driven, the ability to list, add users

7. Add postgres support with tested/mocked management command
   1. run added test
      - `docker-compose run app sh -c "python manage.py test core.tests.test_commands.CommandTests "`
   2. create superuser (optional)
   - `docker-compose run app sh -c "python manage.py createsuperuser"`
   3. bring up containers
      - `docker-compose up -d`
   4. Visit in browser `http://localhost:8000/admin`
