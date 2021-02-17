from django.contrib import admin
from .models import Empresa
from .models import Funcionario

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Funcionario)
