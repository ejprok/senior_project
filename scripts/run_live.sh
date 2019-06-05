pkill gunicorn

gunicorn --daemon --workers 3 --bind unix:/var/www/demo/csforsac/csforsac.sock csforsac.wsgi
