from django.shortcuts import render, redirect
from django.http import HttpResponse

def pagina_login(request):
        
    return render(request, 'login.html')

def pagina_dicas(request):

    return render(request, 'dicas.html')

def pagina_home