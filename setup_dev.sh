#!/bin/sh

echo ">>> Iniciando o PostgreSQL..."
service postgresql start

echo ">>> Criando o banco de dados 'digitalsys'..."
psql -U postgres -c "CREATE DATABASE digitalsys"

echo ">>> Executando migrações..."
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createcachetable

echo ">>> Criando superusuário..."
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

echo ">>> Iniciando o worker do Celery..."
celery -A celery_tasks worker -Q default -l INFO --detach

echo ">>> Populando a tabela SetUserFormConfiguration..."
python3 manage.py ONEOFF_set_user_form_configuration

echo ">>> Iniciando o servidor Django..."
python3 manage.py runserver 0.0.0.0:8000
