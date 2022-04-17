from django.urls import path

from . import views

urlpatterns = [
    path('', views.comunidades, name='comunidades'),
    path('sangabriel/', views.sangabriel, name='sangabriel'),
    path('jorco/', views.jorco, name='jorco'),
    path('acosta/', views.acosta, name='acosta'),
    path('tarbaca/', views.tarbaca, name='tarbaca'),
]