from django.shortcuts import render, redirect
from django.http import HttpResponse

def pagina_login(request):
        
    #return redirect('login')
    return render(request, 'login.html')