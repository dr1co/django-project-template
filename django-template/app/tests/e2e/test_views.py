"""
E2E Tests for the Template Views.

Minimum expected coverage per view (see AGENTS.md, Tests section): status
code 200, or a redirect when the view is protected by @auth_required and
there's no session.

Example:

    class HomeViewTest(TestCase):
        def test_home_status_code(self):
            # Simulates a request to the root route
            response = self.client.get("/")
            # Checks the response status is 200 (OK)
            self.assertEqual(response.status_code, 200)

    class ProtectedViewTest(SessionTestCase):
        def test_redirects_without_session(self):
            response = self.client.get("/dashboard")
            self.assertEqual(response.status_code, 302)

        def test_status_code_with_session(self):
            self.login_as_user()
            response = self.client.get("/dashboard")
            self.assertEqual(response.status_code, 200)
"""
from . import SessionTestCase  # noqa: F401

# Create your view tests here.
