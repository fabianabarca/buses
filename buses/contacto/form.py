# Formulario de la app de contacto
from django import forms

# FIXME: Agregar la lista a la base de datos
asuntos = [
    ('horario', 'Consulta de horario'),
    ('perdidos', 'Objetos extraviados'),
    ('sugerencia', 'Sugerencias'),
    ('queja', 'Denuncias'),
    ('otro', 'Otros')
]

class Formulario(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    asunto = forms.CharField(required=True,
                             label='¿Cuál es el motivo de consulta?',
                             widget=forms.Select(choices=asuntos)
    )
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

#    TODO: agregar la lista de asuntos recurrentes
