from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Comunidad(models.Model):
    nombre = models.CharField(max_length=32)
    resena = RichTextField(blank=True, null=True)
    imagen = models.ImageField(default=None)
    url = models.CharField(max_length=32, 
                help_text="Identificador en la URL, ejemplo: sangabriel")
    poblacion = models.PositiveIntegerField(default=0)
    area = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    codigo_postal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre