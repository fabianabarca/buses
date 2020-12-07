from django.shortcuts import render
from noticias.models import Noticia, Aviso

# Create your views here.

def noticias(request):

    # Cargar todas las noticias y avisos
    todas_noticias = Noticia.objects.all()
    todos_avisos = Aviso.objects.all()

    context = {
        'todas_noticias': todas_noticias, 
        'todos_avisos': todos_avisos
    }

    return render(request, 'noticias.html', context)

def noticia(request):
    return render(request, 'noticia.html')

def crear_url(noticia_titulo):
    url = 42

    return url

def busqueda(request):

    elemento_Deseado = request.GET['elemento_Busqueda']

    if elemento_Deseado:
        noticias_Relacionadas=Noticia.objects.filter(titulo__icontains=elemento_Deseado)
        avisos_Relacionados=Aviso.objects.filter(titulo__icontains=elemento_Deseado)
        return render(request,'busqueda.html',{"elemento_Deseado":elemento_Deseado,'noticias_Relacionadas':noticias_Relacionadas,'avisos_Relacionados':avisos_Relacionados})
    
    else:
        return  render(request,'noticias.html')
    