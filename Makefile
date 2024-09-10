install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C tcoki

test:
	pytest -vv --cov-report term-missing --cov=tcoki test_*.py

format:
	black *.py
