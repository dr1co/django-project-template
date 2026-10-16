"""
Models and Database Connections configuration.

This file plays two key roles in this template's architecture:

1. Native Django ORM Models:
    Used to structure the application's internal database (local tables).
    Django manages relationships, type mapping and migrations automatically.

    Example:
    class Employee(models.Model):
        name = models.CharField(max_length=100)
        department = models.CharField(max_length=50)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            # Sets the exact name of the local table
            db_table = "tb_employee"


2. Connections to External Databases (SQLAlchemy via BaseDBConnector):
    For queries against legacy databases, ERPs or external integrated
    servers (via raw SQL). To use it, create a specialized class that
    inherits from `BaseDBConnector` and set the connection string for the
    target database's dialect.
    Inside the child class, you can also create specific methods that call
    the base methods, to keep queries and parameters organized.

    Usage example:
    class CorporatePostgresConnector(BaseDBConnector):
        def __init__(self, host, port, user, passwd, db):
            super().__init__(host, port, user, passwd, db)
            # Builds the specific string (e.g. PostgreSQL via psycopg)
            self.conn_string = (
                f"postgresql+psycopg://{self._username}:{self._password}"
                f"@{self._host}:{self._port}/{self._database}"
            )
"""

import traceback
from urllib.parse import quote_plus

import sqlalchemy as sqla
from django.db import models  # noqa: F401

# ==============================================================================
# 1. DJANGO ORM MODELS
# ==============================================================================
# Create your local Django models below:


# ==============================================================================
# 2. EXTERNAL DATABASE CONNECTORS
# ==============================================================================
# Base class for connections to external databases
class BaseDBConnector:
    def __init__(self, host, port, user, passwd, db):
        self._host = quote_plus(str(host))
        self._port = quote_plus(str(port))
        self._username = quote_plus(str(user))
        self._password = quote_plus(str(passwd))
        self._database = quote_plus(str(db))

        self.conn_string = ""
        self._engine = None

    def print_connection(self):
        return print(self.conn_string)

    def engine(self):
        if self.conn_string == "":
            raise ValueError("Database connection not specified.")

        if self._engine is None:
            self._engine = sqla.create_engine(
                self.conn_string,
                pool_recycle=1800,
                pool_pre_ping=True,
                max_overflow=0,
                pool_size=5,
            )

        return self._engine

    def fetchone_read_query(self, query: str = None, params: dict = None):
        if query is None:
            return None

        params = params or {}

        try:
            with self.engine().connect() as connection:
                result = connection.execute(sqla.text(query), params)
                rows = result.fetchall()
                columns = result.keys()

                data = [dict(zip(columns, row)) for row in rows]

                return data[0] if data else None
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
            tb_str = traceback.format_exc()
            print(f"\n{tb_str}")
            return None

    def fetchall_read_query(self, query: str = None, params: dict = None):
        if query is None:
            return None

        params = params or {}

        try:
            with self.engine().connect() as connection:
                result = connection.execute(sqla.text(query), params)
                rows = result.fetchall()
                columns = result.keys()

                data = [dict(zip(columns, row)) for row in rows]

                return data if data else []
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
            tb_str = traceback.format_exc()
            print(f"\n{tb_str}")
            return None

    def execute_write_query(self, query: str = None, params: dict = None):
        if query is None:
            return False

        params = params or {}

        try:
            with self.engine().begin() as connection:
                result = connection.execute(sqla.text(query), params)

                return result.rowcount > 0
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
            tb_str = traceback.format_exc()
            print(f"\n{tb_str}")
            return False
