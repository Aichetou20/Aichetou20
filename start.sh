#!/bin/bash
set -e

# Wait for postgres
echo "Waiting for postgres..."
while ! nc -z db23029 5432; do
    sleep 1
done
echo "PostgreSQL started"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn INPC.wsgi:application -c gunicorn_config.py
