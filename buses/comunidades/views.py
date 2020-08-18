from django.shortcuts import render

# Create your views here.

def comunidades(request):
    return render(request, 'comunidades.html')

def comunidad(request):
    return render(request, 'comunidad.html')