from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Comunidad(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.CharField(
        max_length=255, 
        default='Descripción',
        help_text='Descripción corta para la página principal de comunidades')
    resena = RichTextField(blank=True, null=True)
    url = models.CharField(max_length=32, 
                help_text="Identificador en la URL, ejemplo: sangabriel")
    poblacion = models.PositiveIntegerField(default=0)
    area = models.DecimalField(
        default=0, 
        max_digits=6, 
        decimal_places=2)
    latitud = models.DecimalField(
        default=1.0,
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 del centro de la comunidad')
    longitud = models.DecimalField(
        default=1.0,
        max_digits=22,
        decimal_places=16,
        help_text='WGS 84 del centro de la comunidad')
    codigo_postal = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(
        upload_to='comunidades',
        blank=True)

    def __str__(self):
        return self.nombre