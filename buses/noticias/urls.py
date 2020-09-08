from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<fecha>/<int:noticia_id>', views.noticia, name='noticia'),
    path('busqueda/', views.busqueda, name='busqueda')
]
