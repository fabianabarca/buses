from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.acerca, name='acerca'),
    path('gtfs/', views.gtfs, name='gtfs'),
    path('covid19/', views.covid19, name='covid19'),
    path('presentacion/', views.presentacion, name='presentacion'),
]