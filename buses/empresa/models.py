from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=32)
    contenido = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
