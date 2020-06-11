ENV=$(CURDIR)/.env
BIN=$(ENV)/bin

RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


all: env
	@echo "Virtualenv is installed"


.PHONY: clean
# target: clean - Display callable targets
clean:
	@rm -rf build pydist docs/_build
	@rm -f *.py[co]
	@rm -f *.orig
	@rm -f *.prof
	@rm -f *.lprof
	@rm -f *.so
	@rm -f */*.py[co]
	@rm -f */*.orig
	@rm -f */*/*.py[co]

.PHONY: upload
# target: upload - Upload module on PyPi
upload:
	@python setup.py sdist --dist-dir pydist bdist_wheel --dist-dir pydist upload || echo 'Upload already'

.PHONY: test
# target: test - Runs tests
test: clean
	$(BIN)/nose2

.PHONY: lint
# target: lint - audit code
lint:
	@tox -e pylama

.PHONY: env
# target: env - install python develpment packages
env:
	@python3 -m venv $(ENV)
	$(ENV)/bin/pip install -r requirements-dev.txt

.PHONY: build
# target: build - build self-executable tabtools scripts
build:
	bash build.sh
