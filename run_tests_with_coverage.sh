#!/usr/bin/env bash

. ~/.virtualenvs/python2.7/bin/activate

rm -f pep8.log pyflakes.log

PYTHONPATH=. python -m coverage run number_system_xmlrunner.py

python -m coverage xml -o coverage.xml
python -m coverage html -d coverage

# TODO(dhanraju): Check the given directory depth covers all .py files.
pylint --rcfile=pylint.cfg $(find . -maxdepth 2 -name "*.py" -print) main/ > pylint.log || exit 0

# pep8 --max-line-length=120 pystache > pep8.log || true
# pyflakes pystache > pyflakes.log || true
