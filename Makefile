# Makefile to simplify repetitive build env management tasks under posix

CODESPELL_DIRS ?= ./pyaedt
CODESPELL_SKIP ?= "*.pyc,*.xml,*.txt,*.gif,*.png,*.jpg,*.js,*.html,*.doctree,*.ttf,*.woff,*.woff2,*.eot,*.mp4,*.inv,*.pickle,*.ipynb,flycheck*,./.git/*,./.hypothesis/*,*.yml,./docs/build/*,./docs/images/*,./dist/*,*~,.hypothesis*,./docs/source/examples/*,*cover,*.dat,*.mac,\#*,PKG-INFO,*.mypy_cache/*,*.xml,*.aedt,*.svg"
CODESPELL_IGNORE ?= "ignore_words.txt"

all: doctest flake8

doctest: codespell

codespell:
	@echo "Running codespell"
	@codespell $(CODESPELL_DIRS) -S $(CODESPELL_SKIP) # -I $(CODESPELL_IGNORE)

flake8:
	@echo "Running flake8"
	@flake8 .

docker-pull:
	@pip install docker
	@bash .ci/pull_syc_image.sh

build-install:
	#@pip install -r requirements/requirements_build.txt
	@pip install build
	@python -m build
	@pip install -q --force-reinstall dist/*.whl

generate-api:
	@echo "Generate API classes"
	@python -m venv env_generate
	@. env_generate/bin/activate
	@pip install -e .
	@pip install -r requirements/requirements_classesgen.txt
	@python scripts/generate_datamodel.py
	@rm -rf env_generate

unittest:
	@echo "Running unit tests (including coverage)"
	#@pip install -r requirements/requirements_test.txt
	@python -m pip install .[tests]
	@pytest -v --cov=ansys.systemcoupling --cov-report xml --cov-report html:cov_html --cov-report term:skip-covered --cov-config=.coveragerc
