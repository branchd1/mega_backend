release: python3 manage.py migrate && python3 manage.py collectstatic --no-input
web: gunicorn mega_backend.wsgi