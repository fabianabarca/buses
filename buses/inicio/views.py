from django.shortcuts import get_object_or_404, render
from rutas.models import Route, FeedInfo
from datetime import datetime
from os import popen as bash

# Create your views here.

def index(request):
    rutas = Route.objects.all()
    ahora = datetime.now()
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    fecha = [dias[ahora.weekday()], ahora.day, meses[ahora.month - 1], ahora.year]
    context = {
        'rutas': rutas, # Lista de rutas
        'fecha': fecha,
    }
    return render(request, 'index.html', context)

def acerca(request):
    try:
        # La version del sitio se puede definir como el commit que se está utilizando, así como la fecha de creación del mismo.
        version = bash("echo $(git branch --show-current) $( git reflog --pretty='%h -> %cD' | head -n 1 | cut -f -6 --delimiter=' ' )").read()
    except:
        # La version no funciona para Windows, está pensada para Ubuntu Server
        version = 'UNKNOWN'

    context ={
        'version': version,
    }
    return render(request, 'acerca.html', context)

def gtfs(request):
    informacion = FeedInfo.objects.get(pk=1)
    context = {
        'informacion': informacion
    }
    return render(request, 'gtfs.html', context)

def covid19(request):
    return render(request, 'covid19.html')

def presentacion(request):
    return render(request, 'presentacion.html')
