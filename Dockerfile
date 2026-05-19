# Usamos Python 3.12 en su versión liviana
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero requirements para aprovechar caché de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Puerto que expone Django
EXPOSE 8000

# Comando para arrancar el servidor en producción
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]