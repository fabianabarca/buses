# Formulario de la app de contacto
from django import forms

class Formulario(forms.Form):
    email = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

#    TODO: agregar la lísta de asuntos recurrentes
