"""
Application configuration (AppConfig).

This file contains the app's metadata class, used by Django to register
and identify this module within the project.

You usually won't need to change this file, unless you need to run code
automatically when the server starts (such as connecting Signals).

For more information on the application lifecycle, see:
    https://docs.djangoproject.com/en/6.0/ref/applications/

Example of automatic initialization (Signals):

    class MyAppConfig(AppConfig):
        default_auto_field = "django.db.models.BigAutoField"
        name = "your_app_name"

        def ready(self):
            # Code placed here runs ONCE, as soon as
            # the Django server finishes starting up.
            import your_app_name.signals
"""
from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
