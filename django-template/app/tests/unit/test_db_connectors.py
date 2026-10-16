"""
Unit Tests for the External Database Connectors (BaseDBConnector).

Never connect to a real external database in these tests — mock the
SQLAlchemy engine/connection with unittest.mock. The contract to validate is
the one in app/models.py:
    fetchone_read_query  -> dict | None (None on error)
    fetchall_read_query  -> list[dict]  (None on error)
    execute_write_query  -> bool        (False on error)

Example:

    from unittest.mock import patch

    from app.models import BaseDBConnector

    class BaseDBConnectorTest(TestCase):
        def test_fetchone_returns_none_on_error(self):
            connector = BaseDBConnector(
                "host", "port", "user", "password", "db"
            )
            # Avoids the empty-connection ValueError
            connector.conn_string = "sqlite://"

            with patch.object(
                connector, "engine", side_effect=Exception("failure")
            ):
                result = connector.fetchone_read_query("SELECT 1")

            self.assertIsNone(result)
"""
from django.test import TestCase  # noqa: F401

# Create your connector tests here.
