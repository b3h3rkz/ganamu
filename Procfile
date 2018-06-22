web: gunicorn config.wsgi:application
worker: celery worker --app=namu.taskapp --loglevel=info
