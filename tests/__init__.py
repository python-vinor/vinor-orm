# -*- coding: utf-8 -*-

import sys
import os
from unittest import TestCase
from vinorm.database_manager import DatabaseManager
from .orm.models import Model, User

PY2 = sys.version_info[0] == 2

if PY2:
    import mock
else:
    import unittest.mock as mock


class VinormTestCase(TestCase):
    def tearDown(self):
        if hasattr(self, "local_database"):
            os.remove(self.local_database)

    def init_database(self):
        self.local_database = "/tmp/vinorm_test_database.db"

        if os.path.exists(self.local_database):
            os.remove(self.local_database)

        self.manager = DatabaseManager(
            {
                "default": "sqlite",
                "sqlite": {"driver": "sqlite", "database": self.local_database},
            }
        )

        with self.manager.transaction():
            try:
                self.manager.statement(
                    "CREATE TABLE `users` ("
                    "id INTEGER PRIMARY KEY NOT NULL, "
                    "name CHAR(50) NOT NULL, "
                    "created_at DATETIME DEFAULT CURRENT_TIMESTAMP, "
                    "updated_at DATETIME DEFAULT CURRENT_TIMESTAMP"
                    ")"
                )
            except Exception:
                pass

        Model.set_connection_resolver(self.manager)

        self.manager.disconnect()

    def assertRegex(self, *args, **kwargs):
        if PY2:
            return self.assertRegexpMatches(*args, **kwargs)
        else:
            return super(VinormTestCase, self).assertRegex(*args, **kwargs)

    def assertNotRegex(self, *args, **kwargs):
        if PY2:
            return self.assertNotRegexpMatches(*args, **kwargs)
        else:
            return super(VinormTestCase, self).assertNotRegex(*args, **kwargs)
