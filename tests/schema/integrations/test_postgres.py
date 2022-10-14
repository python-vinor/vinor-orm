# -*- coding: utf-8 -*-

import os
from ... import VinorTestCase
from vinor.connections import PostgresConnection
from vinor.connectors.postgres_connector import PostgresConnector
from . import IntegrationTestCase


class SchemaBuilderPostgresIntegrationTestCase(IntegrationTestCase, VinorTestCase):
    @classmethod
    def get_connection_resolver(cls):
        return DatabaseIntegrationConnectionResolver()


class DatabaseIntegrationConnectionResolver(object):

    _connection = None

    def connection(self, name=None):
        if self._connection:
            return self._connection

        ci = os.environ.get("CI", False)
        if ci:
            database = "vinor_test"
            user = "postgres"
            password = None
        else:
            database = "vinor_test"
            user = "vinor"
            password = "vinor"

        self._connection = PostgresConnection(
            PostgresConnector().connect(
                {"database": database, "user": user, "password": password}
            )
        )

        return self._connection

    def get_default_connection(self):
        return "default"

    def set_default_connection(self, name):
        pass
