from django.shortcuts import get_object_or_404, render
from .models import Nota

# Create your views here.

from .models import Funcionario

def empresa(request):
    empresa = Nota.objects.all()
    contexto = {
        'empresa': empresa
    }
    return render(request, 'empresa.html', contexto)

def personal(request):
    funcionarios = Funcionario.objects.all()
    contexto = {
        'funcionarios': funcionarios,
    }
    return render(request, 'personal.html', contexto)

def funcionario(request, func_id):
    funcionario = get_object_or_404(Funcionario, id=func_id)
    contexto = {
        'funcionario': funcionario,
    }
    return render(request, 'funcionario.html', contexto)
