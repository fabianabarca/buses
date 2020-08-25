from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=256)
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta