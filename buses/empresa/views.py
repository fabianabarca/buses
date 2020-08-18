from django.shortcuts import render

# Create your views here.

def empresa(request):
    return render(request, 'empresa.html')

def personal(request):
    return render(request, 'personal.html')