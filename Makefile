# Makefile - just runs program , runs tests, and creates docs
#
all:	docs

docs:
		sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html

test:
		nosetests tests

run:
		python src/casm.py

.PHONY:	run docs test
