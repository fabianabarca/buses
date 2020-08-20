from django.urls import path

from . import views

app_name = 'comunidades'

urlpatterns = [
    path('', views.comunidades, name='comunidades'),
    path('<url_comunidad>/', views.comunidad, name='comunidad'),
]