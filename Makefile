install:

	pip install -r requirements.txt

clean:

	find -name *.pyc -delete

migrations:

	python manage.py makemigrations

migrate:

	python manage.py migrate

run: clean migrate

	python manage.py runsslserver

test:

	echo "tests not implemented yet"
