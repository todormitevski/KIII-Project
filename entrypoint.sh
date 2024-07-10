#!/bin/bash

DB_HOST="${DB_HOST:-db}"

echo "Waiting for database..."
while ! nc -z $DB_HOST 5432; do
  sleep 1
done
echo "Database ready"

python manage.py collectstatic --noinput
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser --noinput --username admin --email "" --password admin || true

python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username='admin', email='', password='admin');
"

exec gunicorn --bind 0.0.0.0:8080 eventProject.wsgi:application
