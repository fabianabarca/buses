from django.shortcuts import get_object_or_404, render
from .models import Empresa
from .models import Funcionario

# Create your views here.

def empresa(request):
    empresa = get_object_or_404(Empresa, codigo='TSG')
    funcionarios = Funcionario.objects.all()
    context = {
        'empresa': empresa,
        'funcionarios': funcionarios
    }
    return render(request, 'empresa.html', context)

def personal(request):
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionarios': funcionarios,
    }
    return render(request, 'personal.html', context)

def funcionario(request, func_id):
    funcionario = get_object_or_404(Funcionario, id=func_id)
    context = {
        'funcionario': funcionario,
    }
    return render(request, 'funcionario.html', context)
