#!/bin/sh

# Stops at the first failing step instead of reporting a broken project as created.
set -e

ARG_1=$1

# Without a host directory mounted here, the project would be created inside
# the container and lost when it exits.
if ! grep -qs " $(pwd) " /proc/mounts; then
  echo "Error: no host directory is mounted at $(pwd)." >&2
  echo "Run the generator with: docker run --rm -it -v \"\$PWD:$(pwd)\" <image> [project_name]" >&2
  exit 1
fi

if [ -z "$ARG_1" ]; then
  echo "======================="
  echo "=== DJANGO TEMPLATE ==="
  echo "======================="

  printf "Enter your application name [default: main_app]: "
  read -r INPUT_NAME

  APP_NAME=${INPUT_NAME:-main_app}
else
  APP_NAME=$ARG_1
fi

WORKSPACE=$(pwd)
PROJECT_DIR="$WORKSPACE/$APP_NAME"

# The container runs as root, so everything it creates would be root-owned on
# the host. On exit (success or failure), hand the project over to whoever owns
# the mounted directory, i.e. the user who ran `docker run`.
fix_ownership() {
  if [ -d "$PROJECT_DIR" ]; then
    chown -R "$(stat -c '%u:%g' "$WORKSPACE")" "$PROJECT_DIR"
  fi
}
trap fix_ownership EXIT

echo "Creating project $APP_NAME..."
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo "Starting the Django structure..."
django-admin startproject core .

echo "Creating the default app: 'app'..."
python manage.py startapp app

echo "Copying template files..."
cp -ar /app/generator/django-template/. .

# startapp's tests.py clashes with the template's app/tests/ package.
rm -f app/tests.py

echo "Setting up .env..."
NEW_SECRET=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

cat << EOF > .env
DJANGO_SECRET_KEY=$NEW_SECRET
DJANGO_DEBUG_MODE="True"
DJANGO_ALLOWED_HOSTS="*"
EOF

echo "Applying base migrations..."
mkdir data
python manage.py migrate

echo "Setting up the TailwindCSS environment..."
python manage.py tailwind init --app-name=theme --tailwind-version=4s --no-input

echo "Applying the design system to the Tailwind source..."
cp /app/generator/tailwind/styles.css theme/static_src/src/styles.css

echo "Enabling the 'theme' module in settings.py..."
sed -i 's/# #TAILWIND_THEME_PLACEHOLDER#/"theme",/g' "core/settings.py"

echo "Building the TailwindCSS file..."
python manage.py tailwind install
python manage.py tailwind build

echo "Preparing the repository and requirements.txt..."
pip freeze > requirements.txt
git init

echo "==============================================="
echo "✨ Django project and app created successfully!"
echo "==============================================="

echo "Go to your new application's folder with 'cd $APP_NAME/'."
