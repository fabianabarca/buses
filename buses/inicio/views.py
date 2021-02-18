from django.shortcuts import get_object_or_404, render
from rutas.models import Route
from .models import Prueba

# Create your views here.

def index(request):
    rutas = Route.objects.all()
    context = {
        'rutas': rutas, # Lista de rutas      
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'acerca.html')

def prueba(request):
    personas = Prueba.objects.all()
    context = {
        'personas': personas,
    }
    return render(request, 'prueba.html', context)