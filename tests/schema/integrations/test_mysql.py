# -*- coding: utf-8 -*-

import os
from ... import VinormTestCase
from vinorm.connections import MySQLConnection
from vinorm.connectors.mysql_connector import MySQLConnector
from . import IntegrationTestCase


class SchemaBuilderMySQLIntegrationTestCase(IntegrationTestCase, VinormTestCase):
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
            user = "root"
            password = ""
        else:
            database = "vinorm_test"
            user = "vinorm"
            password = "vinorm"

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
