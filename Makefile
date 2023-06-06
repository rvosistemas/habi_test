clean:
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf ./.cache .mypy_cache ./schema/.mypy_cache .coverage

PROJECT = app
COVFILE ?= .coverage

linux-coverage-app: 
	export COVERAGE_FILE=$(COVFILE); pytest --cov=$(PROJECT) tests/ \
	--cov-report term-missing -x -s -W ignore::DeprecationWarning -o cache_dir=/tmp/application/cache

windows-coverage-app: 
	set COVERAGE_FILE=$(COVFILE) && pytest --cov=$(PROJECT) tests/ \
	--cov-report term-missing -x -s -W ignore::DeprecationWarning -o cache_dir=/tmp/application/cache