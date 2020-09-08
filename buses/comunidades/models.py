from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Comunidad(models.Model):
    nombre = models.CharField(max_length=32)
    resena = RichTextField(blank=True, null=True)
    url = models.CharField(max_length=32)
    poblacion = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    codigo_postal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre