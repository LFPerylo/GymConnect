from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados 
from .models import Feedback
from .forms import FeedbackForm 
from .forms import ProgressoForm
from .models import Duvida
from .models import Consulta
from .forms import CadastroForm, LoginForm


def login(request):
        
    return render(request, 'front/login.html')

def cadastro(request):

    return render(request, 'front/cadastro.html')

def dicas(request):

    return render(request, 'dicas.html')

def home_aluno(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            return redirect('/home_adm/')
        elif tipo == 'aluno':
            return redirect('/home_aluno/')
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
        nome = request.POST.get('nome')
        senha = make_password(request.POST.get('senha'))  # Usa hashing para a senha

        # Criando um novo registro com as informações coletadas do formulário
        registro = Dados(tipo=tipo, nome=nome, senha=senha)
        registro.save()  # Salva o novo registro no banco de dados

        # Redireciona com base no tipo de usuário
        if tipo == 'administrador':
            return redirect('/home_adm/')
        elif tipo == 'usuario':
            return redirect('/home_aluno/')  # Mudança aqui para alinhar com a opção correta
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


def enviar_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home_aluno.html', {'message': 'Feedback registrado com sucesso!'})
            
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def registrar_progresso(request):
    if request.method == 'POST':
        form = ProgressoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProgressoForm()
    return render(request, 'progresso.html', {'form': form})

def enviar_duvida(request):
    if request.method == 'POST':
        duvida_escrita = request.POST.get('duvidaescrita')
        nome_treinador = request.POST.get('treinador')
        
        # Crie um novo objeto de Duvida e salve no banco de dados
        duvida = Duvida(duvida_escrita=duvida_escrita, nome_treinador=nome_treinador)
        duvida.save()
        
        # Retorna uma resposta para o usuário
        return redirect('/')
    else:
        return redirect('/')
    

def enviar_feedback(request):
    if request.method == 'POST':
        duvida_escrita = request.POST.get('duvidaescrita')
        nome_treinador = request.POST.get('treinador')
        
        # Crie um novo objeto de Duvida e salve no banco de dados
        duvida = Duvida(duvida_escrita=duvida_escrita, nome_treinador=nome_treinador)
        duvida.save()
        
        # Retorna uma resposta para o usuário
        return redirect('/')
    else:
        return redirect('/')
    

def agendar_consulta(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        mensagem = request.POST.get('mensagem', '')  # Mensagem é opcional

        # Salvar no banco de dados
        consulta = Consulta(data=data, horario=horario, mensagem=mensagem)
        consulta.save()

        # Redirecionar para alguma página de sucesso
        return redirect('pagina_sucesso')

    return render(request, 'sua_template.html')

def progresso(request):
    # Recupere todos os progressos salvos no banco de dados
    progressos = ProgressoForm.objects.all()
    
    # Passe os progressos para o template como contexto
    return render(request, 'progresso.html', {'progressos': progressos})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})


def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            Dados = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if Dados:
                if Dados.tipo == 'usuario':
                    # Redirecionar usuário para a página home do aluno
                    return redirect('/home_aluno/')
                elif Dados.tipo == 'administrador':
                    # Redirecionar administrador para a página home do administrador
                    return redirect('/home_adm/')
            else:
                # Exibir uma mensagem de erro
                return render(request, 'login.html', {'form': form, 'erro': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'erro': False})
