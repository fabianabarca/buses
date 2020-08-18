from django.shortcuts import render

# Create your views here.

def noticias(request):
    return render(request, 'noticias.html')