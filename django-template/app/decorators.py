"""
Custom Decorators for the app.

This file is NOT created by Django by default, but it's used to centralize
functions that intercept and modify the behavior of your Views (business
rules, security checks, permission checks, etc.). This also includes
context handling.

A decorator works as an "extra layer" wrapped around your View function,
running BEFORE the View actually processes the request.

How it works:
We use `functools.wraps` to preserve the original function's metadata.

Below is an example using the user context.
"""
from functools import wraps

from django.shortcuts import redirect

# Create your decorators here.


def auth_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_data = request.session.get("user_data", None)

        if not user_data:
            return redirect("/")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
