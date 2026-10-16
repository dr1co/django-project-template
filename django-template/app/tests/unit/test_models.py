"""
Unit Tests for the Django ORM Models.

Minimum expected coverage per model (see AGENTS.md, Tests section): a test
that creates an instance and checks its fields.

Example:

    from app.models import Employee

    class EmployeeModelTest(TestCase):
        def test_create_employee(self):
            # Creates a test record in the in-memory database
            employee = Employee.objects.create(name="John", department="IT")
            # Checks the data was saved correctly
            self.assertEqual(employee.name, "John")
"""
from django.test import TestCase  # noqa: F401

# Create your model tests here.
