from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from rutas.models import Agency
from .models import Pregunta
from .form import Formulario

def contacto(request):

    # Estado del formulario
    enviado = False

    if request.method == 'GET':
        formulario = Formulario()
    else:
        formulario = Formulario(request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data['email']
            asunto = formulario.cleaned_data['asunto']
            mensaje = formulario.cleaned_data['mensaje']
            # try: # FIXME: implementar correctamente la configuración de SMTP
            #     send_mail(asunto, mensaje, email, ['admin@tsgcr.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            enviado = True

    empresa = get_object_or_404(Agency, agency_id=1234)
    preguntas = Pregunta.objects.all()
    notificacion = "Listo!, gracias por su mensaje" # FIXME: agregar modelo a la base de datos
    contexto = {
        'empresa': empresa,
        'preguntas': preguntas,
        'formulario': formulario,
        'enviado': enviado,
        'notificacion': notificacion,
    }
    return render(request, 'contacto.html', contexto)
