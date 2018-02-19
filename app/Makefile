freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

run:
	gunicorn app:app --preload

heroku_push:
	git push heroku master