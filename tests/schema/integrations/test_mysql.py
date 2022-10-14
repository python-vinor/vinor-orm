# -*- coding: utf-8 -*-

import os
from ... import VinorTestCase
from vinor.connections import MySQLConnection
from vinor.connectors.mysql_connector import MySQLConnector
from . import IntegrationTestCase


class SchemaBuilderMySQLIntegrationTestCase(IntegrationTestCase, VinorTestCase):
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
            user = "root"
            password = ""
        else:
            database = "vinor_test"
            user = "vinor"
            password = "vinor"

        self._connection = MySQLConnection(
            MySQLConnector().connect(
                {"database": database, "user": user, "password": password}
            )
        )

        return self._connection

    def get_default_connection(self):
        return "default"

    def set_default_connection(self, name):
        pass
