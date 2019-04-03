# djangorestframework-recipe

A showcase djangorestframework api for creating and finding recipes.

---

## Commit Steps

1. Simple docker install. Python container with Django and DRF

   To invoke, run `docker build .`

2. Create docker-compose app service and created an empty django app

   `docker-compose run app sh -c "django-admin.py startproject app."`

3. Add flake8 and Travis-CI configuration
