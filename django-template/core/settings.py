"""
Django settings for the core project, responsible for managing the apps
and the structure of the project.

Written manually for this template, with a few additional settings.
(Current compatibility version: 6.0.5)

For more information on this file, see:
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Environment variables go here.
# SECRET_KEY is already set up to be read from an environment variable.
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")


# DEBUG MODE: use True for development. When deploying, ALWAYS SET IT TO False.
DEBUG = os.getenv("DJANGO_DEBUG_MODE", "False") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # Main app registration. If more apps are created in the same
  # project, they must be registered here.
  'app',

  # Apps required by TailwindCSS
  'tailwind',
  # #TAILWIND_THEME_PLACEHOLDER#
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',

        # Comment out the line below to disable the custom
        # context. See the path below for more information.
        'app.context.global_data',
      ],
    },
  },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Django's database, for internal processing. More information at:
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'data' / 'db.sqlite3',
  }
}

# Cache configuration.
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    'LOCATION': 'cache_table',
    'TIMEOUT': 3600,
  },
}


# Password validation for the admin users. Usually not used by the
# application itself.
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]


# Internationalization and locales
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SESSION_COOKIE_AGE = 1209600

SESSION_EXPIRE_AT_BROWSER_CLOSE = False


# Static files (CSS, JavaScript, Images)
# Already pre-configured, more information at the link below:
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'app', STATIC_URL),
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# TailwindCSS configuration
TAILWIND_APP_NAME = 'theme'
