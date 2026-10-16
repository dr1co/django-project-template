"""
URL configuration for the app.

This is where the application's routes are actually written. Import the
app's views and bind them to routes, following the examples below.

More information on structuring routes in the "core.urls" guide.

By convention, it's good practice to name the view after the route it
is served on. The same goes for the route name.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("logged-in", views.logged_in_view, name="logged_in_view"),
    path("logged-out", views.logged_out_view, name="logged_out_view"),
]
