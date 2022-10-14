# -*- coding: utf-8 -*-

from .. import VinormTestCase
from . import IntegrationTestCase


class SQLiteIntegrationTestCase(IntegrationTestCase, VinormTestCase):
    @classmethod
    def get_manager_config(cls):
        return {
            "default": "sqlite",
            "sqlite": {"driver": "sqlite", "database": ":memory:"},
        }
