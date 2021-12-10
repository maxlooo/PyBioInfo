.PHONY: test

test:
	python3 -m pytest -xv fib.py tests/fib_test.py

# https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop
#	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy fib.py tests/fib_test.py

all:
	../bin/all_test.py fib.py
