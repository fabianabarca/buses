from django.shortcuts import render

# Create your views here.

def rutas(request):
    return render(request, 'rutas.html')

def ruta(request):
    return render(request, 'ruta.html')