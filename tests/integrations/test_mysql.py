# -*- coding: utf-8 -*-

import os

from .. import VinorTestCase
from . import IntegrationTestCase


class MySQLIntegrationTestCase(IntegrationTestCase, VinorTestCase):
    @classmethod
    def get_manager_config(cls):
        ci = os.environ.get("CI", False)

        if ci:
            database = "vinor_test"
            user = "root"
            password = ""
        else:
            database = "vinor_test"
            user = "vinor"
            password = "vinor"

        return {
            "default": "mysql",
            "mysql": {
                "driver": "mysql",
                "database": database,
                "user": user,
                "password": password,
            },
        }

    def get_marker(self):
        return "%s"
