#!/bin/sh

set -e

echo "=== Applying Django database migrations..."
python manage.py migrate --noinput

echo "=== Creating cache table..."
python manage.py createcachetable

echo "=== Building the TailwindCSS file..."
python manage.py tailwind build

echo "=== Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Entrypoint finished! Starting the server with Gunicorn ==="
exec "$@"
