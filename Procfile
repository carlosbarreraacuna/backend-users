web: gunicorn apiusers.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn apisuers.wsgi