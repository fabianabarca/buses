from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Comunidad

def comunidades(request):
    comunidades = Comunidad.objects.all()
    contexto = {
        'comunidades': comunidades
    }
    return render(request, 'comunidades.html', contexto)

def comunidad(request, url_comunidad):
    comunidad = get_object_or_404(Comunidad, url=url_comunidad)
    contexto = {
        'comunidad': comunidad,
    }
    return render(request, 'comunidad.html', contexto)