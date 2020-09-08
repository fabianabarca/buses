from django.urls import path

from . import views

urlpatterns = [
    path('', views.empresa, name='empresa'),
    path('personal/', views.personal, name='personal'),
    path('funcionario_<func_id>',
         views.funcionario, name='funcionario'),
]
