from django.urls import path

from . import views

app_name = 'ruta'

urlpatterns = [
    path('', views.rutas, name='rutas'),
    path('<url_ruta>/', views.ruta, name='ruta'),
    path('proximobus/<url_ruta>/', views.proximo_bus, name='proximo_bus'),
]