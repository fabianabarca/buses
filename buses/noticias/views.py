from django.shortcuts import render
from noticias.models import Noticia,Aviso

# Create your views here.

def noticias(request):

    #Para cargar todas las noticias y avisos
    todas_noticias = Noticia.objects.all()
    todos_avisos = Aviso.objects.all()

    return render(request, 'noticias.html',{'todas_noticias':todas_noticias, 'todos_avisos':todos_avisos})

def noticia(request):
    return render(request, 'noticia.html')

def busqueda(request):

    elemento_Deseado=request.GET['elemento_Busqueda']

    if elemento_Deseado:
        noticias_Relacionadas=Noticia.objects.filter(titulo__icontains=elemento_Deseado)
        avisos_Relacionados=Aviso.objects.filter(titulo__icontains=elemento_Deseado)
        return render(request,'busqueda.html',{"elemento_Deseado":elemento_Deseado,'noticias_Relacionadas':noticias_Relacionadas,'avisos_Relacionados':avisos_Relacionados})
    
    else:
        return  render(request,'noticias.html')
    