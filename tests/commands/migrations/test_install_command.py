# -*- coding: utf-8 -*-

from flexmock import flexmock
from vinorm.migrations import DatabaseMigrationRepository
from vinorm.commands.migrations import InstallCommand
from .. import VinormCommandTestCase


class MigrateInstallCommandTestCase(VinormCommandTestCase):
    def test_execute_calls_repository_to_install(self):
        repo_mock = flexmock(DatabaseMigrationRepository)
        repo_mock.should_receive("set_source").once().with_args("foo")
        repo_mock.should_receive("create_repository").once()

        command = flexmock(InstallCommand())
        command.should_receive("_get_config").and_return({})

        self.run_command(command, [("--database", "foo")])
