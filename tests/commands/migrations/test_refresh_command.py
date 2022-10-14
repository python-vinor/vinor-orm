# -*- coding: utf-8 -*-

import os
from flexmock import flexmock
from vinorm.migrations import Migrator
from vinorm.commands.migrations import RefreshCommand
from vinorm import DatabaseManager
from .. import VinormCommandTestCase


class RefreshCommandTestCase(VinormCommandTestCase):
    def test_refresh_runs_the_seeder_when_seed_option_set(self):
        resolver = flexmock(DatabaseManager)
        resolver.should_receive("connection").and_return(None)

        command = flexmock(RefreshCommand())
        command.should_receive("_get_config").and_return({})
        command.should_receive("confirm").and_return(True)
        command.should_receive("call").with_args("migrate:reset", object).and_return(
            True
        )
        command.should_receive("call").with_args("migrate", object).and_return(True)
        command.should_receive("_run_seeder")

        self.run_command(command, [("--seed")])

    def test_refresh_does_not_run_the_seeder_when_seed_option_absent(self):
        resolver = flexmock(DatabaseManager)
        resolver.should_receive("connection").and_return(None)

        command = flexmock(RefreshCommand())
        command.should_receive("_get_config").and_return({})
        command.should_receive("confirm").and_return(True)
        command.should_receive("call").with_args("migrate:reset", object).and_return(
            True
        )
        command.should_receive("call").with_args("migrate", object).and_return(True)

        self.run_command(command, [])
