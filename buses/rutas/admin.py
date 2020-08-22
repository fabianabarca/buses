from django.contrib import admin

# Register your models here.

from .models import Ruta, Agency

admin.site.register(Ruta)
admin.site.register(Agency)