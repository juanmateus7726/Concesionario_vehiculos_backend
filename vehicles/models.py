from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    year = models.PositiveIntegerField(verbose_name="Año")
    locality = models.CharField(max_length=200, verbose_name="Localidad")
    applicant = models.CharField(max_length=200, verbose_name="Aspirante")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"