from django.urls import path

from . import views

urlpatterns = [
    path('', views.rutas, name='rutas'),
    path('sangabriel/', views.ruta, name='sangabriel'),
    path('acosta/', views.ruta, name='acosta'),
]