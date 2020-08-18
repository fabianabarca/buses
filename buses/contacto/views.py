from django.shortcuts import render

# Create your views here.

def contacto(request):
    return render(request, 'contacto.html')