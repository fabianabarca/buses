from django.db import models

# Create your models here.

class Comunidad(models.Model):
    nombre = models.CharField(max_length=32)
    resena = models.TextField('Reseña de la comunidad')
    url = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre