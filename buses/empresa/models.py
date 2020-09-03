from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=32)
    contenido = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Funcionario(models.Model):
    identificacion = models.IntegerField()

    # Prueba
    url_site = models.CharField(max_length=256)

    nombre = models.CharField(max_length=256)
    # apellido_a = models.CharField(max_length=256)
    # apellido_b = models.CharField(max_length=256)
    cargo = models.CharField(max_length=256)
    # nacimiento = models.DateField()

    # FIXME:
    def __str__(self):
        return self.nombre
