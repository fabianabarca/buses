from django.shortcuts import render

# Create your views here.

def noticias(request):
    return render(request, 'noticias.html')

def noticia(request):
    return render(request, 'noticia.html')