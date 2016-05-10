all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

test: clean
	app/manage.py collectstatic --noinput
	app/manage.py test test

database:
	app/manage.py makemigrations
	app/manage.py migrate
	app/manage.py syncdb

run_app: clean
	app/manage.py runserver 0.0.0.0:9000