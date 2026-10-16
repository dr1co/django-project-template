"""
Automated Tests for the Application.

This app's tests are organized into two packages, by type:

    app/tests/
    ├── unit/   # Models and BaseDBConnector (external calls always mocked)
    └── e2e/    # Views (HTTP requests simulated via self.client)

Expected workflow (TDD): write the test before the code, watch it fail, then
implement until it passes. Exceptions are documented in AGENTS.md (Tests
section): purely visual/copy changes, configuration/routing, and refactors
with no behavior change under already-green tests.

To run the tests, run this in the container's terminal:
    python manage.py test

For more information on testing in Django, see:
    https://docs.djangoproject.com/en/6.0/topics/testing/
"""
