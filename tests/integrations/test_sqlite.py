# -*- coding: utf-8 -*-

from .. import VinorTestCase
from . import IntegrationTestCase


class SQLiteIntegrationTestCase(IntegrationTestCase, VinorTestCase):
    @classmethod
    def get_manager_config(cls):
        return {
            "default": "sqlite",
            "sqlite": {"driver": "sqlite", "database": ":memory:"},
        }
