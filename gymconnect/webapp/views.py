from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados  # Certifique-se de que o nome da classe está em CamelCase como é padrão

def login(request):
        
    return render(request, 'front/login.html')

def dicas(request):

    return render(request, 'dicas.html')

def home_aluno(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            return redirect('/home_adm')
        elif tipo == 'aluno':
            return redirect('/home_aluno')
        else:
            return HttpResponse("Usuário ou senha inválidos", status=401)
    return render(request, 'home_aluno.html')

def home_adm(request):
    usuarios = Dados.objects.all()  # Obtém todos os usuários do banco de dados
    return render(request, 'home_adm.html', {'usuarios': usuarios})

@csrf_exempt
def processar_formulario(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        usuario = request.POST.get('usuario')
        senha = make_password(request.POST.get('senha'))  # Usa hashing para a senha

        # Criando um novo registro com as informações coletadas do formulário
        registro = Dados(tipo=tipo, usuario=usuario, senha=senha)
        registro.save()  # Salva o novo registro no banco de dados

        # Redireciona com base no tipo de usuário
        if tipo == 'administrador':
            return redirect('/home_adm')
        elif tipo == 'usuario':
            return redirect('/home_aluno')  # Mudança aqui para alinhar com a opção correta
        else:
            return redirect('/')  # Redireciona para a página inicial se o tipo não for válido

    # Retorna um erro se o método da requisição não for POST
    return JsonResponse({'error': 'Método não permitido'}, status=405)



def duvidas(request):

    return render(request,'duvidas.html')

def treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')

def marcar_consulta(request):

    return render(request, 'marcar_consulta.html')

def progresso(request):

    return render(request,'progresso.html')

def feedback(request):

    return render(request,'feedback.html')