from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Usuario con rol. Extiende el usuario base de Django.
    No repetimos toda la lógica de auth — solo agregamos el campo 'role'.
    """

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        VIEWER = 'viewer', 'Viewer'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.VIEWER,
    )

    def is_admin(self) -> bool:
        """Retorna True si el usuario tiene rol admin."""
        return self.role == self.Role.ADMIN

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"