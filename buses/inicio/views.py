from django.shortcuts import get_object_or_404, render

# Create your views here.

from rutas.models import Route

def index(request):
    # rutas = Ruta.objects.all()
    contexto = {
        # 'rutas': rutas,
    }
    return render(request, 'index.html', contexto)