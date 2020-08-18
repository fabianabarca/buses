from django.urls import path

from . import views

urlpatterns = [
    path('', views.comunidades, name='comunidades'),
    path('sangabriel/', views.comunidad, name='comunidad'),
    path('acosta/', views.comunidad, name='comunidad'),
]