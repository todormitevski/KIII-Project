#!/bin/bash

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database ready"

python manage.py migrate

exec gunicorn --bind 0.0.0.0:8080 eventProject.wsgi:application