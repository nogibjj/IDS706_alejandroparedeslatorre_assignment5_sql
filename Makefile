install:
	pip install -r requirements.txt
format:
	black *.py
lint:
	ruff check *.py ./lib/*.py
test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_main.py

run_cli:
	python main.py extract
	python main.py load
	python main.py create "John Doe" USA US California example.com example.com
	python main.py read
	python main.py update 1 "John Campbell" BOL BO "Santa Cruz" example2.com example2.com
	python main.py delete 1

all: install format test lint run_cli