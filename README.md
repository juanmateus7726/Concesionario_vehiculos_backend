# Backend - Formulario Vehiculos

-Desarrollado con Django, para gestion de vehiculos de un concesionario, incluye autenticacion JWT, control de acceso por roles RBAC, loggin avanzado y recuperacion de contrasena por correo.


-Stack Tecnologias

Python 3.12
Django 5.0
Django REST Framework
SimpleJWT
PostgreSQL 15
Docker + Docker Compose


-Estructura del Proyecto

backend-vehiculos/
├── config/
│   ├── settings.py        # Configuración global
│   └── urls.py            # Rutas principales
├── core/
│   └── middleware.py      # Logging de requests HTTP
├── users/
│   ├── models.py          # Modelo de usuario con roles
│   ├── views.py           # Login y registro
│   ├── serializers.py     # Serialización de datos
│   └── password_reset.py  # Recuperación de contraseña
├── vehicles/
│   ├── models.py          # Modelo de vehículo
│   ├── views.py           # CRUD de vehículos
│   ├── serializers.py     # Serialización de vehículos
│   └── permissions.py     # Permisos por rol
├── Dockerfile
└── requirements.txt


-Autenticacion y Roles

El sistema usa JWT (JSON Web Tokens) con dos roles:

*Admin: CRUD completo(crear, editar, eliminar vehiculos)
*Viewer: Solamente lectura(listar y ver vehiculos)

Los tokens tienen una vida de 16 minutos.


-Endpoints

Auth

Metodo      Endpoint                        Descripcion                     Auth
POST    /api/auth/register/                 Registro de usuario             No
POST    /api/auth/login/Login/              retorna JWT                     No
POST    /api/auth/refresh/                  Renovar token                   No
POST    /api/auth/password-reset/           Enviar correo de recuperación   No
POST    /api/auth/password-reset/confirm/   Confirmar nueva contraseña      No

Vehiculos

Metodo      Endpoind                        Descripcion                     Auth
GET         /api/vehicles/                  Listar vehículos                Admin/Viewer
POST        /api/vehicles/                  Crear vehículo                  Admin
PATCH       /api/vehicles/{id}/             Editar vehículo                 Admin
DELETE      /api/vehicles/{id}/             Eliminar vehículo               Admin


-Instalacion y Ejecucion Local

Requisitos
*Docker Desktop instalado

Pasos en Terminal

1. Clonar el repositorio
   git clone https://github.com/juanmateus7726/Concesionario_vehiculos_backend

2. Entrar a la carpeta raiz del proyecto
   cd Prueba_Vehiculos

3. Levantar los contenedores
   docker-compose up --build

4. En otra terminarl, aplicar migraciones
   docker-compose exec backend python manage.py migrate

-Principios Aplicados

SOLID — Cada clase tiene una sola responsabilidad
Clean Code — Nombres descriptivos, funciones pequeñas, comentarios útiles
Logging avanzado — Cada request registra método, ruta, status, tiempo y usuario
RBAC — Control de acceso granular por rol
Seguridad — Contraseñas hasheadas, tokens JWT de corta vida

Usuario Administrador

Usuario: admin
Contrasena: Admin1234

Usuario Visita

Usuario: viewer
Contrasena: Viewer1234