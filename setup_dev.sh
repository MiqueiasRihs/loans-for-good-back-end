#!/bin/sh

echo xxxxxxxxxxxxxxx MIGRATIONS xxxxxxxxxxxxxxx

python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

echo xxxxxxxxxxxxxxx CREATE USER xxxxxxxxxxxxxxx

python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

echo xxxxxxxxxxxxxxx RUN PROJECT xxxxxxxxxxxxxxx

python manage.py runserver 0.0.0.0:8000