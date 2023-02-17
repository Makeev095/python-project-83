dev:
	poetry run flask --app page_analyzer:app run

install: 
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

lint:
	poetry run flake8 page_analyzer

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) app:main