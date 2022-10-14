# -*- coding: utf-8 -*-

import os

from .. import VinorTestCase
from . import IntegrationTestCase


class PostgresQmarkIntegrationTestCase(IntegrationTestCase, VinorTestCase):
    @classmethod
    def get_manager_config(cls):
        ci = os.environ.get("CI", False)

        if ci:
            database = "vinor_test"
            user = "postgres"
            password = None
        else:
            database = "vinor_test"
            user = "vinor"
            password = "vinor"

        return {
            "default": "postgres",
            "postgres": {
                "driver": "pgsql",
                "database": database,
                "user": user,
                "password": password,
                "use_qmark": True,
            },
        }

    def get_marker(self):
        return "?"
