all_targets: lint test clean-pyc clean-files

lint:
	flake8 --ignore E501 *.py

test:
	python3 tests.py

clean-pyc:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

clean-files:
	find . -name "*.html" -delete

help:
	@echo "    lint"
	@echo "        Check PEP8 compliance with flake8."
	@echo "    test"
	@echo "        Run all tests in spidy/tests.py."
	@echo "    clean-pyc"
	@echo "        Remove Python artifacts."
