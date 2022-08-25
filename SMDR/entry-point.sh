#!/bin/bash
# python manage.py makemigrations
python manage.py makemigrations account --noinput
python manage.py makemigrations appiontment --noinput
python manage.py migrate --noinput

# echo "admin" | python manage.py createsuperuser --username admin --email admin@admin.com --first_name admin
python manage.py authconfig
exec "$@"
