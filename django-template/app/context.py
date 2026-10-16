"""
Context Processors for the app.

This file is NOT created by Django by default, but it's extremely useful for
defining functions that inject global variables into ALL HTML templates
automatically, without having to pass them explicitly in each view.

For these functions to work, they must be registered in the
"OPTIONS -> context_processors" list inside the TEMPLATES setting in your
`core/settings.py`.

How it works:
Each function must accept the `request` object as an argument and MUST
return a Python dictionary (dict). The keys of this dictionary become
available as variables in Django Templates.

Below is an example for the logged-in user context. The default shape of
"user_data" looks like this:

user_data = {
    "user_reg": user's registration number,
    "name": name,
    "email": email,
}

The variable is exposed as `current_user` (not `user`) so it doesn't shadow
the `user` variable from django.contrib.auth's context processor.
"""

# Create your context processors here.


def global_data(request):
    user = request.session.get("user_data", None)

    context = {
        "current_user": user,
    }

    return context
