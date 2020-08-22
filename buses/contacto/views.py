from django.shortcuts import get_object_or_404, render

# Create your views here.

from rutas.models import Agency
from .models import Pregunta

def contacto(request):
    empresa = get_object_or_404(Agency, agency_id=1234)
    preguntas = Pregunta.objects.all()
    contexto = {
        'empresa': empresa,
        'preguntas': preguntas,
    }
    return render(request, 'contacto.html', contexto)