run:
	poetry run gunicorn --bind 0.0.0.0:5000 --workers 8 src.main:app

test:
	poetry run pytest tests/
