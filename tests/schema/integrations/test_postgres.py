# -*- coding: utf-8 -*-

import os
from ... import VinormTestCase
from vinorm.connections import PostgresConnection
from vinorm.connectors.postgres_connector import PostgresConnector
from . import IntegrationTestCase


class SchemaBuilderPostgresIntegrationTestCase(IntegrationTestCase, VinormTestCase):
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
            database = "vinorm_test"
            user = "postgres"
            password = None
        else:
            database = "vinorm_test"
            user = "vinorm"
            password = "vinorm"

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
