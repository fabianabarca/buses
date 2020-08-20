from django.urls import path

from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<fecha>/<int:noticia_id>', views.noticia, name='noticia')
]