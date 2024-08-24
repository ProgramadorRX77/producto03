from django.db import models

class Producto(models.Model):
    TIPO_CHOICES = [
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to='productos_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.descripcion
