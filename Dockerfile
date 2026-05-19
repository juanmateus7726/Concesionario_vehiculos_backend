FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py shell -c \"from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').delete(); U.objects.create_superuser('admin', 'admin@admin.com', 'Admin1234')\" && python manage.py runserver 0.0.0.0:8000"]