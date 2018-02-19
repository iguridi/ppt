freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

run:
	gunicorn app:app --preload

heroku_push:
	git push heroku master

new_gitignore:
	git rm -r --cached .
	git add .
	git commit -m 'new gitignore'