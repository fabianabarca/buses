from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    edad = models.PositiveIntegerField()

    # Para mostrar el nombre en el admin
    def __str__(self):
        return self.nombre