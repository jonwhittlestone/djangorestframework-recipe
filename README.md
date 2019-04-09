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

1. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/4a76bb968d4dbbe897cc34b4d618088f45eb4872) Simple docker install. Python container with Django and DRF

   To invoke, run `docker build .`

2. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/9345b01cc913cdb6cddd510fa6c6ce2188bab5ef)Create docker-compose app service and created an empty django app

   `docker-compose run app sh -c "django-admin.py startproject app."`

3. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/d733adc891a1f326245646ac6b031de359725fc8)Add flake8 and Travis-CI configuration

4. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/d31b27d480799af16c534b71f44be61d1628577a)Create `core` app with separate tests directory

5. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/88dbf0ecb0836f6f173f7b95b44fc395ac1d9f34)Configure Custom User Model to use email not username (plus some tests)

6. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/9345b01cc913cdb6cddd510fa6c6ce2188bab5ef) Setting up Django Admin. Test-Driven, the ability to list, add users

7. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/96ad21870191114c1c57255e29d51516f1eb3f0d)Add postgres support with tested/mocked management command

   1. run added test
      - `docker-compose run app sh -c "python manage.py test core.tests.test_commands.CommandTests "`
   2. create superuser (optional)

   - `docker-compose run app sh -c "python manage.py createsuperuser"`

   3. bring up containers
      - `docker-compose up -d`
   4. Visit in browser `http://localhost:8000/admin`

8. [[commit]](https://github.com/jonwhittlestone/djangorestframework-recipe/commit/77ce19e9e4f51a53b3bfb554565d68b2368fa807) Add drf and API endpoints and tests for adding and authenticating users

   - example CURL statement for manual replication

     ```
      POST /api/user/create/? HTTP/1.1
      Host: 127.0.0.1:8000
      Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
      Accept: application/json
      cache-control: no-cache
      Postman-Token: 06ad72c6-8f61-46cc-bc45-8959aeebef3c

      Content-Disposition: form-data; name="email"

      user@howapped.com

      Content-Disposition: form-data; name="password"

      test1

      Content-Disposition: form-data; name="name"

      user
      ------WebKitFormBoundary7MA4YWxkTrZu0gW--
     ```

9. Add test and API endpoints for modifying a user
