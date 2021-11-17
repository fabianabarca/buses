from django.db import models
from ckeditor.fields import RichTextField

# Create your models here. (Hola)

class Empresa(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=64)
    resena = RichTextField(blank=True, null=True)
    colaboradores = models.PositiveIntegerField(help_text="Número de colaboradores.")
    buses = models.PositiveIntegerField(help_text="Número de buses.")
    fundacion = models.PositiveIntegerField(help_text="Año de fundación.")
    direccion = models.CharField(max_length=256, help_text="Dirección de oficinas centrales.")

    def __str__(self):
        return self.nombre

class Funcionario(models.Model):
    identificacion = models.IntegerField()

    # Prueba
    url_site = models.SlugField(max_length=256)

    nombre = models.CharField(max_length=256)
    # apellido_a = models.CharField(max_length=256)
    # apellido_b = models.CharField(max_length=256)
    cargo = models.CharField(max_length=256)
    # nacimiento = models.DateField()

    # FIXME:
    def __str__(self):
        return self.nombre
