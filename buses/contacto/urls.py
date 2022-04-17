from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('post_form', views.post_contact_form, name='post_contact_form')
]
