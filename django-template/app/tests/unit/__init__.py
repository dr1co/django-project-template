"""
Unit Tests.

Cover models (Django ORM) and external database connectors (BaseDBConnector).
Nothing here should depend on the network or a real external database: calls
through SQLAlchemy are always mocked with unittest.mock (patch/patch.object).
"""
