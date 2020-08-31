from django.contrib import admin

from noticias.models import Noticia, Aviso

# Register your models here.
# Para manejar la visualización de los modelos en Admin. Incluir motores de búsqueda, etc.

class AvisoAdmin(admin.ModelAdmin):
    list_display=('titulo','fecha_publicacion','urgencia')
    list_filter=('urgencia',)
    search_fields=('titulo','descripcion')

class NoticiaAdmin(admin.ModelAdmin):
    list_display=('titulo','fecha_publicacion','descripcion_Corta')
    list_filter=('fecha_publicacion',)
    search_fields=('titulo','descripcion_Corta')


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Aviso, AvisoAdmin)