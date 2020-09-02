from django.shortcuts import render
from .models import Nota

# Create your views here.

def empresa(request):
    empresa = Nota.objects.all()
    contexto = {
        'empresa': empresa
    }
    return render(request, 'empresa.html', contexto)

def personal(request):
    return render(request, 'personal.html')



