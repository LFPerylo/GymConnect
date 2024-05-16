from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados, Dica
from .models import Feedback
from .forms import FeedbackForm 
from .forms import ProgressoForm
from .models import Duvida
from .models import Consulta,TreinoPredefinido
from .forms import CadastroForm, LoginForm, DicaForm,ConsultaForm,TreinoPredefinidoForm
from .models import Imagem
from datetime import datetime


def login(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/login.html', {'imagens': imagens})

def cadastro(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/cadastro.html', {'imagens': imagens})

def dicas(request):

    return render(request, 'dicas.html')

def dicas_adm(request):

    return render(request, 'dicas_adm.html')

def home_aluno(request, nome_usuario=None):
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
    return render(request, 'home_aluno.html', {'nome_usuario': nome_usuario})

def home_adm(request):
    usuarios = Dados.objects.all()  # Obtém todos os usuários do banco de dados
    return render(request, 'home_adm.html', {'usuarios': usuarios})

def duvidas(request):

    return render(request,'duvidas.html')

def treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')

def treinospredefinidos_adm(request):

    return render(request, 'treinospredefinidos_adm.html')

def marcar_consulta(request):

    return render(request, 'marcar_consulta.html')

def marcar_consulta_adm(request):

    return render(request,'marcar_consulta_adm.html')

def progresso(request):

    return render(request,'progresso.html')

def feedback(request):

    return render(request,'feedback.html')

def feedback_aluno(request):

    return render(request, 'feedback_aluno.html')

def registrar_progresso(request):
    if request.method == 'POST':
        form = ProgressoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/progresso/')
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
        return redirect('/duvidas/')
    else:
        return redirect('/duvidas/')
    

def enviar_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            feedback_texto = form.cleaned_data['feedback']

            # Verificar se o aluno existe e é do tipo "usuário"
            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                aluno = Dados.objects.get(nome=nome_aluno)
                feedback = Feedback.objects.create(feedback=feedback_texto, aluno=aluno)
                return redirect('/feedback/')  # Redirecionar para página de sucesso
            else:
                form.add_error('nome_aluno', 'Aluno não encontrado ou não é um usuário.')

    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('/marcar_consulta/')  
    else:
        form = ConsultaForm() 

    return render(request, 'marcar_consulta.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
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
            # Consulta ao banco de dados para verificar o usuário
            usuario = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if usuario:
                if tipo == 'usuario':
                    # Redirecionar usuário para a página home do aluno
                    return redirect('/home_aluno/')  # Passando o nome do usuário como parte da URL
                elif tipo == 'administrador':
                    # Redirecionar administrador para a página home do administrador
                    return redirect('/home_adm/')
            
            erro = 'Usuário não cadastrado ou credenciais incorretas.'
    else:
        form = LoginForm()
        erro = None
    return render(request, 'front/login.html', {'form': form, 'erro': erro})

def adicionar_dica(request):
    if request.method == 'POST':
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dicas_adm/')
    else:
        form = DicaForm()
    return render(request, 'dicasadm.html', {'form': form})

def exibir_dica(request):
    tipo_selecionado = request.GET.get('tipo')
    dicas = Dica.objects.filter(tipo=tipo_selecionado) if tipo_selecionado else None
    return render(request, 'dicas.html', {'dicas': dicas})

def criar_treino_predefinido(request):
    if request.method == 'POST':
        form = TreinoPredefinidoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para alguma página de sucesso
            return redirect('/treinospredefinidos_adm/')  # substitua '/sucesso/' pela URL da página de sucesso desejada
    else:
        form = TreinoPredefinidoForm()

    return render(request, 'treinospredefinidos_adm.html', {'form': form})


def exibir_treino_predefinido(request):
    tipo_treino = request.GET.get('tipo_treino')
    treinos = None
    
    if tipo_treino:
        treinos = TreinoPredefinido.objects.filter(tipo_treino=tipo_treino)
    
    return render(request, 'treinospredefinidos.html', {'treinos': treinos})

def exibir_feedback(request):
    if request.method == 'GET':
        nome_aluno = request.GET.get('nome_aluno')

        if nome_aluno:
            try:
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                feedbacks = Feedback.objects.filter(aluno=aluno)
                return render(request, 'feedback_aluno.html', {'feedbacks': feedbacks, 'nome_aluno': nome_aluno})
            except Dados.DoesNotExist:
                mensagem_erro = "Aluno não encontrado no banco de dados."
            except Feedback.DoesNotExist:
                mensagem_erro = "Não há feedback para este aluno."
            except Exception as e:
                mensagem_erro = str(e)

            return render(request, 'feedback_aluno.html', {'mensagem_erro': mensagem_erro})

        else:
            return render(request, 'feedback_aluno.html')

    return render(request, 'feedback_aluno.html')

def exibir_consultas(request):
    if request.method == 'GET':
        data_selecionada = request.GET.get('data')
        if data_selecionada:
            try:
                # Converta a data de string para o formato de data do Python
                data_selecionada = datetime.strptime(data_selecionada, '%Y-%m-%d').date()
                consultas = Consulta.objects.filter(data=data_selecionada)
                return render(request, 'marcar_consulta_adm.html', {'consultas': consultas, 'data_selecionada': data_selecionada})
            except ValueError:
                mensagem_erro = "Formato de data inválido."
                return render(request, 'marcar_consulta_adm.html', {'mensagem_erro': mensagem_erro})
        else:
            mensagem_erro = "Nenhuma data selecionada."
            return render(request, 'marcar_consulta_adm.html', {'mensagem_erro': mensagem_erro})
    else:
        # Se não for um método GET, redirecione ou retorne algo apropriado
        pass

