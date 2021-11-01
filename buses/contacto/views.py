from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

from rutas.models import Agency
from .models import Pregunta
from .form import Formulario

@require_POST
def post_contact_form (request):
    formulario = Formulario(request.POST)
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        email = formulario.cleaned_data['email']
        asunto = formulario.cleaned_data['asunto']
        mensaje = formulario.cleaned_data['mensaje']
        mensaje = mensaje + "\nEnviado por el usuario: " +\
            nombre + '[' + email + ']'

        try: # FIXME: implementar correctamente la configuración de SMTP usando correo del administrador que está en base de datos
            send_mail(asunto, mensaje, email, ['tsgdumbacc@gmail.com'])
            # send_mail("Mensaje recibido", "Agredecemos su aporte.", 'tsgdumbacc@gmail.com', [email]) # TODO remove

        except BadHeaderError:
            return JsonResponse(status=500, data={"message": "Ha ocurrido un error, por favor intente más tarde, gracias."})

    return JsonResponse(status=200, data={"message": '<i class="fas fa-info-circle"></i> Formulario <strong>enviado</strong> correctamente! Gracias!'})

@require_GET
def contacto(request):
    formulario = Formulario()
    empresa = get_object_or_404(Agency, agency_id='TSG')

    preguntas = Pregunta.objects.all()
    antes = preguntas.filter(categoria = -1)
    durante = preguntas.filter(categoria = 0)
    despues = preguntas.filter(categoria = 1)

    contexto = {
        'empresa': empresa,
        'antes': antes,
        'durante': durante,
        'despues': despues,
        'formulario': formulario,
    }

    return render(request, 'contacto.html', contexto)
