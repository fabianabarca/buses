from django.db import models

# Create your models here.

class Ruta(models.Model):
    route_id = models.IntegerField()
    agency_id = models.CharField(max_length=16)
    route_short_name = models.CharField(max_length=16)
    route_long_name = models.CharField(max_length=32)

    def __str__(self):
        return self.route_short_name