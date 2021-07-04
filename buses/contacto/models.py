from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=512)
    respuesta = models.TextField()
    categoria = models.IntegerField(default='',
        choices=(
            (-1, 'Antes'),
            ( 0, 'Durante'),
            ( 1, 'Después'),
        )
    )

    def __str__(self):
        return self.pregunta