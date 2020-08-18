from django.urls import path

from . import views

urlpatterns = [
    path('', views.empresa, name='empresa'),
    path('personal/', views.personal, name='personal'),
]