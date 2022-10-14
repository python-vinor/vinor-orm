# -*- coding: utf-8 -*-

import os

from .. import VinormTestCase
from . import IntegrationTestCase


class MySQLIntegrationTestCase(IntegrationTestCase, VinormTestCase):
    @classmethod
    def get_manager_config(cls):
        ci = os.environ.get("CI", False)

        if ci:
            database = "vinorm_test"
            user = "root"
            password = ""
        else:
            database = "vinorm_test"
            user = "vinorm"
            password = "vinorm"

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
