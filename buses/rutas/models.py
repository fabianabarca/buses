from django.db import models

# Create your models here.

class Agency(models.Model):
    """One or more transit agencies that provide the data in this feed.
    Maps to agency.txt in the GTFS feed.
    """
    agency_id = models.CharField(
        max_length=255, blank=True, db_index=True,
        help_text="Unique identifier for transit agency"
        )
    name = models.CharField(
        max_length=255,
        help_text="Full name of the transit agency"
        )
    url = models.URLField(
        blank=True, help_text="URL of the transit agency"
        )
    timezone = models.CharField(
        max_length=255,
        help_text="Timezone of the agency"
        )
    lang = models.CharField(
        max_length=2, blank=True,
        help_text="ISO 639-1 code for the primary language"
        )
    phone = models.CharField(
        max_length=255, blank=True,
        help_text="Voice telephone number"
        )
    fare_url = models.URLField(
        blank=True, help_text="URL for purchasing tickets online"
        )
    email = models.EmailField(max_length=254,  blank=True, help_text="Customer Service email")

    def __str__(self):
        return self.name

class Ruta(models.Model):
    route_id = models.IntegerField()
    agency_id = models.CharField(max_length=16)
    route_short_name = models.CharField(max_length=16)
    route_long_name = models.CharField(max_length=32)

    def __str__(self):
        return self.route_short_name