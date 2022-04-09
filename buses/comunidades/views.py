from django.shortcuts import render

# Create your views here.

def comunidades(request):
    return render(request, 'comunidades.html')

def sangabriel(request):
    return render(request, 'sangabriel.html')

def jorco(request):
    return render(request, 'jorco.html')

def acosta(request):
    return render(request, 'acosta.html')

def tarbaca(request):
    return render(request, 'tarbaca.html')