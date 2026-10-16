"""
E2E Tests (Views).

Simulate real HTTP requests via self.client. For screens protected by
@auth_required, use SessionTestCase below instead of writing
session["user_data"] by hand in every test.
"""
from django.test import TestCase


class SessionTestCase(TestCase):
  """
  TestCase with a helper to simulate a logged-in user.

  The session is written manually because this template doesn't use
  django.contrib.auth (see AGENTS.md, Authentication and session section).
  """

  def login_as_user(self, **data):
    session = self.client.session
    session["user_data"] = {
      "user_reg": "0001",
      "name": "Test User",
      "email": "test@example.com",
      **data,
    }
    session.save()
