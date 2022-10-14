# -*- coding: utf-8 -*-

from .. import VinorTestCase

from vinor.connections.mysql_connection import MySQLConnection


class MySQLConnectionTestCase(VinorTestCase):
    def test_marker_is_properly_set(self):
        connection = MySQLConnection(None, "database", "", {"use_qmark": True})

        self.assertEqual("?", connection.get_marker())

    def test_marker_default(self):
        connection = MySQLConnection(None, "database", "", {})

        self.assertIsNone(connection.get_marker())

    def test_marker_use_qmark_false(self):
        connection = MySQLConnection(None, "database", "", {"use_qmark": False})

        self.assertIsNone(connection.get_marker())
