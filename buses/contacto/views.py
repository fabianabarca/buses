from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_GET, require_POST

from django.conf import settings
import json
import requests

# Create your views here.

from rutas.models import Agency
from .models import Pregunta
from .form import Formulario

@require_POST
def post_contact_form (request):

    formulario = Formulario(request.POST)
    if not formulario.is_valid():
        return JsonResponse(status=500, data={"message": "Ha ocurrido un error, por favor intente nuevamente, gracias."})

    nombre = formulario.cleaned_data['nombre']
    email = formulario.cleaned_data['email']
    asunto = formulario.cleaned_data['asunto']
    telefono = formulario.cleaned_data['telefono']
    mensaje = formulario.cleaned_data['mensaje']

    if telefono:
        mensaje = "{}\n\nEnviado por el usuario: {}\nCorreo: [{}]\nTeléfono: {}"\
        .format(mensaje, nombre, email, telefono)
    else:
        mensaje = "{}\n\nEnviado por el usuario: {}\nCorreo: [{}]"\
        .format(mensaje, nombre, email)

    try:
        telegram_token = settings.TELEGRAM_BOT_TOKEN
        telegram_chat_id = settings.TELEGRAM_ADMIN_GROUP

        res = requests.get(
            "https://api.telegram.org/bot{}/getMe" \
            .format(telegram_token)
        )

        response = json.loads(res.text)

        # Comprobar que es el bot de tsg
        assert (response['result']['username'] == "tsgBusesBot")

        res = requests.get(
            "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}\n\n{}" \
            .format(telegram_token, telegram_chat_id, asunto, mensaje)
        )

        response = json.loads(res.text)
        print(response)

    except:
        print("No telegram bot interface")

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
