#!/bin/sh

set -e

echo "=== Applying Django database migrations..."
python manage.py migrate --noinput

echo "=== Creating cache table..."
python manage.py createcachetable

echo "=== Building the TailwindCSS file..."
python manage.py tailwind build

# The container runs as root and, with docker-compose, /app is the project
# folder bind-mounted from the host. Hand the build output back to the owner of
# that folder so it isn't root-owned on the host (no-op without a bind mount).
chown -R "$(stat -c '%u:%g' /app)" theme/static

echo "=== Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Entrypoint finished! Starting the server with Gunicorn ==="
exec "$@"
