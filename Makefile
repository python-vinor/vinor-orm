# This file is part of vinorm
# https://github.com/sdispater/vinorm

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015 Sébastien Eustace

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies and setup databases
setup: setup-python setup-databases

setup-python:
	@read -p 'Did you create and activated a dedicated virtualenv? [y/N]: '; \
	if [[ $$REPLY = y ]]; then \
		pip install -r tests-requirements.txt; \
	else \
		echo 'Aborting'; exit 1; \
	fi

setup-databases: setup-psql setup-mysql

setup-psql: drop-psql
	@echo 'Setting up PostgreSQL database `vinorm_test`...'
	psql -c 'CREATE DATABASE vinorm_test;' -U postgres
	psql -c "CREATE ROLE vinorm PASSWORD 'vinorm';" -U postgres
	psql -c 'ALTER ROLE vinorm LOGIN;' -U postgres
	psql -c 'GRANT ALL PRIVILEGES ON DATABASE vinorm_test TO vinorm;' -U postgres

drop-psql:
	@type -p psql > /dev/null || { echo 'Install and setup PostgreSQL'; exit 1; }
	@-psql -c 'DROP DATABASE vinorm_test;' -U postgres > /dev/null 2>&1
	@-psql -c 'DROP ROLE vinorm;' -U postgres > /dev/null 2>&1

setup-mysql: drop-mysql
	@echo 'Setting up MySQL database `vinorm_test`...'
	mysql -u root -e 'CREATE DATABASE vinorm_test;'
	mysql -u root -e "CREATE USER 'vinorm'@'localhost' IDENTIFIED BY 'vinorm';"
	mysql -u root -e "USE vinorm_test; GRANT ALL PRIVILEGES ON vinorm_test.* \
		TO 'vinorm'@'localhost';"

drop-mysql:
	@type -p mysql > /dev/null || { echo 'Install and setup MySQL'; exit 1; }
	@-mysql -u root -e 'DROP DATABASE vinorm_test;' > /dev/null 2>&1
	@-mysql -u root -e "DROP USER 'vinorm'@'localhost';" > /dev/null 2>&1

extensions:
	@echo 'Making C extensions'
	cython vinorm/support/_collection.pyx
	cython vinorm/utils/_helpers.pyx

# test your application (tests in the tests/ directory)
test:
	@py.test tests -sq

# run tests against all supported python versions
tox:
	@poet make:setup
	@tox
	@rm -f setup.py
