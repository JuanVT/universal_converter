web: gunicorn control.wsgi --log-file -
web: python my_django_app/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT universal_converter/settings.py