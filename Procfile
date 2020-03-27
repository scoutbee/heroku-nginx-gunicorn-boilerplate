release: cd backend && python manage.py migrate
web: cd backend && ./bin/start-nginx gunicorn wueww.wsgi -p /tmp/app-initialized --log-file - --bind 127.0.0.1:8087