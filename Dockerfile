FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py shell -c \"from users.models import User; User.objects.filter(username__in=['admin','viewer']).delete(); User.objects.create_superuser(username='admin', email='admin@admin.com', password='Admin1234', role='admin'); User.objects.create_user(username='viewer', email='viewer@viewer.com', password='Viewer1234', role='viewer')\" && python manage.py runserver 0.0.0.0:8000"]