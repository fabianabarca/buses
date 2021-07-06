from django.shortcuts import get_object_or_404, render
from rutas.models import Route, FeedInfo
from datetime import datetime

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
    return render(request, 'acerca.html')

def gtfs(request):

    informacion = FeedInfo.objects.get(pk=1)

    context = {
        'informacion': informacion
    }

    return render(request, 'gtfs.html', context)

def presentacion(request):

    return render(request, 'presentacion.html')