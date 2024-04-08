from django.shortcuts import render
from django.http import HttpResponse 

def pagina_login(request):
        
    return render(request, 'login.html')

def pagina_dicas(request):

    return render(request, 'dicas.html')

def pagina_home(request):

    return render(request, 'home.html')

def pagina_duvidas(request):

    return render(request,'duvidas.html')

def pagina_treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')