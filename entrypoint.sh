#!/bin/bash
set -e

# Wait for postgres to be ready
echo "Waiting for postgres..."
while ! nc -z db23029 5432; do
    sleep 1
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
