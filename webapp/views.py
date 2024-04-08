from django.shortcuts import render, redirect

def pagina_login(request):
        
    #return redirect('login')
    return render(request, 'login.html')