from django.shortcuts import get_object_or_404, render
from .models import Route

def rutas(request):
    return render(request, 'rutas.html')

def ruta(request, url_ruta):
    route = get_object_or_404(Route, url=url_ruta)

    context = {
        'route': route,
    }

    return render(request, 'ruta.html', context)