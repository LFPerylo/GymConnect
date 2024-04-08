from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore

def login(request):
        
    return render(request, 'front/login.html')

def dicas(request):

    return render(request, 'dicas.html')

def home(request):

    return render(request, 'home.html')

def duvidas(request):

    return render(request,'duvidas.html')

def treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')