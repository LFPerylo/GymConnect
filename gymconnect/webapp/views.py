from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados, Dica
from .models import Feedback
from .forms import FeedbackForm 
from .forms import ProgressoForm
from .models import Duvida
from .models import Consulta,TreinoPredefinido,Progresso,Duvida,Treino,Metas,Info
from .forms import CadastroForm, LoginForm, DicaForm,ConsultaForm,TreinoPredefinidoForm,DuvidaForm,TreinoForm,TreinoEditForm,NomeAlunoForm,MetasForm,InfoForm
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

def info(request):

    return render(request, 'info.html')

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
    usuarios = Dados.objects.all()  
    return render(request, 'home_adm.html', {'usuarios': usuarios})

def duvidas(request):

    return render(request,'duvidas.html')

def duvidas_adm(request):

    return render(request,'duvidas_adm.html')

def metas(request):

    return render(request, 'metas.html')

def metas_adm(request):

    return render(request,'metas_adm.html')

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

def progresso_adm(request):

    return render(request, 'progresso_adm.html')

def feedback(request):

    return render(request,'feedback.html')

def feedback_aluno(request):

    return render(request, 'feedback_aluno.html')

def treino_personalizado(request):

    return render(request, 'treino_personalizado.html')

def treino_personalizado_adm(request):

    return render(request, 'treino_personalizado_adm.html')

def pagina_editar_treino(request):

    return render(request,'pagina_editar_treino.html')

def registrar_progresso(request):
    mensagem_erro = None
    mensagem_sucesso = None

    if request.method == 'POST':
        form = ProgressoForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            tipo_progresso = form.cleaned_data['tipo_progresso']
            observacao = form.cleaned_data['observacao']
            data = form.cleaned_data['data']

            
            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                
                progresso = Progresso.objects.create(nome_aluno=aluno, tipo_progresso=tipo_progresso, observacao=observacao, data=data)
                mensagem_sucesso = "Progresso registrado com sucesso!"
            else:
                mensagem_erro = "Usuário não cadastrado ou não é aluno."
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        form = ProgressoForm()

    return render(request, 'progresso.html', {'form': form, 'mensagem_erro': mensagem_erro,'mensagem_sucesso':mensagem_sucesso})

def criar_meta(request):
    mensagem_erro = ""
    mensagem_sucesso = ""

    if request.method == 'POST':
        form = MetasForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            try:
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                meta = form.save(commit=False)
                meta.aluno = aluno
                meta.save()
                mensagem_sucesso = "Meta registrada com sucesso!"
            except Dados.DoesNotExist:
                mensagem_erro = "O nome digitado não é aluno."
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        form = MetasForm()

    return render(request, 'metas.html', {
        'form': form,
        'mensagem_erro': mensagem_erro,
        'mensagem_sucesso': mensagem_sucesso,
    })

def cadastrar_info(request):
    mensagem_sucesso=""
    mensagem_erro=''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            professor_nome = form.cleaned_data['professor']
            try:
                professor = Dados.objects.get(nome=professor_nome)
                if professor.tipo == 'usuario':
                    mensagem_erro = "O nome digitado não é de um professor."
                else:
                    form.save()
                    mensagem_sucesso="Informações cadastradas com sucesso"
            except Dados.DoesNotExist:
                mensagem_erro = "Usuário não existente."
    else:
        form = InfoForm()
        
    return render(request, 'info.html', {'form': form, 'mensagem_erro': mensagem_erro,'mensagem_sucesso':mensagem_sucesso})


def enviar_duvida(request):
    mensagem_erro = ""
    mensagem_sucesso = ""
    if request.method == 'POST':
        form = DuvidaForm(request.POST)
        if form.is_valid():
            nome_treinador = form.cleaned_data['nome_treinador']
            duvida_escrita = form.cleaned_data['duvida_escrita']
            
            try:
                treinador = Dados.objects.get(nome=nome_treinador)
                if treinador.tipo == 'administrador':
                    Duvida.objects.create(nome_treinador=treinador, duvida_escrita=duvida_escrita)
                    mensagem_sucesso = "Dúvida enviada com sucesso"
                else:
                    mensagem_erro = "O nome enviado não é professor"
            except Dados.DoesNotExist:
                mensagem_erro = "Professor não encontrado/existente"
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        form = DuvidaForm()
    
    return render(request, 'duvidas.html', {'form': form, 'mensagem_erro': mensagem_erro, 'mensagem_sucesso': mensagem_sucesso})

def enviar_feedback(request):
    mensagem_erro = ""
    mensagem_sucesso = ""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            feedback_texto = form.cleaned_data['feedback']

            
            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                aluno = Dados.objects.get(nome=nome_aluno)
                feedback = Feedback.objects.create(feedback=feedback_texto, aluno=aluno)
                mensagem_sucesso = "Feedback registrado com sucesso!"
            else:
                form.add_error('nome_aluno', 'Aluno não encontrado ou não é um usuário.')
                mensagem_erro = "Aluno não encontrado ou não é um usuário."
                print(mensagem_erro)

    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'mensagem_erro': mensagem_erro, 'mensagem_sucesso': mensagem_sucesso})

def agendar_consulta(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid(): 
            form.save() 
            mensagem_sucesso = "consulta marcada com sucesso"  
    else:
        form = ConsultaForm() 

    return render(request, 'marcar_consulta.html', {'form': form,'mensagem_sucesso': mensagem_sucesso})

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
            
            usuario = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if usuario:
                if tipo == 'usuario':
                    
                    return redirect('/home_aluno/')  
                elif tipo == 'administrador':
                    
                    return redirect('/home_adm/')
            
            erro = 'Usuário não cadastrado ou credenciais incorretas.'
    else:
        form = LoginForm()
        erro = None
    return render(request, 'front/login.html', {'form': form, 'erro': erro})

def adicionar_dica(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem_sucesso= "Dica adicionada com sucesso"
    else:
        form = DicaForm()
    return render(request, 'dicasadm.html', {'form': form, 'mensagem_sucesso':mensagem_sucesso})

def exibir_dica(request):
    tipo_selecionado = request.GET.get('tipo')
    dicas = Dica.objects.filter(tipo=tipo_selecionado) if tipo_selecionado else None
    return render(request, 'dicas.html', {'dicas': dicas})

def criar_treino_predefinido(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = TreinoPredefinidoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem_sucesso= "Treino Criado com sucesso"
            
            
    else:
        form = TreinoPredefinidoForm()

    return render(request, 'treinospredefinidos_adm.html', {'form': form, 'mensagem_sucesso':mensagem_sucesso})

def criar_treino(request):
    mensagem_erro = ""
    mensagem_sucesso = ""
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            tipo_treino = form.cleaned_data['tipo_treino']
            exercicio1_nome = form.cleaned_data['exercicio1_nome']
            exercicio1_repeticoes = form.cleaned_data['exercicio1_repeticoes']
            exercicio1_series = form.cleaned_data['exercicio1_series']
            exercicio2_nome = form.cleaned_data['exercicio2_nome']
            exercicio2_repeticoes = form.cleaned_data['exercicio2_repeticoes']
            exercicio2_series = form.cleaned_data['exercicio2_series']
            exercicio3_nome = form.cleaned_data['exercicio3_nome']
            exercicio3_repeticoes = form.cleaned_data['exercicio3_repeticoes']
            exercicio3_series = form.cleaned_data['exercicio3_series']
            exercicio4_nome = form.cleaned_data['exercicio4_nome']
            exercicio4_repeticoes= form.cleaned_data['exercicio4_repeticoes']
            exercicio4_series= form.cleaned_data['exercicio4_series']

            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                nome_aluno = Dados.objects.get(nome=nome_aluno)
                Treino.objects.create( aluno=nome_aluno,tipo_treino=tipo_treino,exercicio1_nome=exercicio1_nome,exercicio1_repeticoes=exercicio1_repeticoes,exercicio1_series=exercicio1_series,exercicio2_nome=exercicio2_nome,exercicio2_repeticoes=exercicio2_repeticoes,exercicio2_series=exercicio2_series,exercicio3_nome=exercicio3_nome,exercicio3_repeticoes=exercicio3_repeticoes,exercicio3_series=exercicio3_series,exercicio4_nome=exercicio4_nome,exercicio4_repeticoes=exercicio4_repeticoes,exercicio4_series=exercicio4_series)
                
                mensagem_sucesso = "Treino criado com sucesso!"
            else:
                mensagem_erro = "Usuário não cadastrado ou não é aluno."
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        form = TreinoForm()

    return render(request, 'treino_personalizado_adm.html', {'form': form, 'mensagem_erro': mensagem_erro, 'mensagem_sucesso': mensagem_sucesso})

def exibir_treinos(request):
    mensagem_erro = ""
    treinos = None

    if request.method == 'POST':
        nome_aluno_form = NomeAlunoForm(request.POST)
        if nome_aluno_form.is_valid():
            nome_aluno = nome_aluno_form.cleaned_data['nome_aluno']
            try:
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                treinos = Treino.objects.filter(aluno=aluno)
                if not treinos:
                    mensagem_erro = "Não há treinos cadastrados para o aluno."
            except Dados.DoesNotExist:
                mensagem_erro = "O nome selecionado não é aluno."
                
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        nome_aluno_form = NomeAlunoForm()

    return render(request, 'pagina_editar_treino.html', {
        'nome_aluno_form': nome_aluno_form,
        'treinos': treinos,
        'mensagem_erro': mensagem_erro,
    })

def editar_treinos(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)

    if request.method == 'POST':
        form = TreinoEditForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            mensagem_sucesso = "Treino editado com sucesso!"
    else:
        form = TreinoEditForm(instance=treino)

    return render(request, 'pagina_editar_treino.html', {
        'treino_edit_form': form,
        'treinos': Treino.objects.filter(aluno=treino.aluno),
        'nome_aluno_form': NomeAlunoForm(initial={'nome_aluno': treino.aluno.nome}),
    })

def exibir_treino_predefinido(request):
    tipo_treino = request.GET.get('tipo_treino')
    treinos = None
    
    if tipo_treino:
        treinos = TreinoPredefinido.objects.filter(tipo_treino=tipo_treino)
    
    return render(request, 'treinospredefinidos.html', {'treinos': treinos})

def visualizar_treinos(request):
    if request.method == 'GET':
        nome_aluno = request.GET.get('nome_aluno')

        if nome_aluno:
            try:
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                treinos = Treino.objects.filter(aluno=aluno)
                return render(request, 'treino_personalizado.html', {'treinos': treinos, 'nome_aluno': nome_aluno})
            except Dados.DoesNotExist:
                mensagem_erro = "Aluno não encontrado no banco de dados."
            except Treino.DoesNotExist:
                mensagem_erro = "Não há treinos registrados para este aluno."
            except Exception as e:
                mensagem_erro = str(e)

            return render(request, 'treino_personalizado.html', {'mensagem_erro': mensagem_erro})

        else:
            return render(request, 'treino_personalizado.html')

    return render(request, 'treino_personalizado.html')

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
    
        pass

def exibir_progresso(request):
    mensagem_erro = None
    progressos = None

    if request.method == 'POST':
        nome_aluno = request.POST.get('nome_aluno')

       
        if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
            aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
            
            progressos = Progresso.objects.filter(nome_aluno=aluno)
            if not progressos:
                mensagem_erro = "Este usuário não possui nenhum progresso registrado."
        else:
            mensagem_erro = "Usuário não cadastrado ou não é usuário."

    return render(request, 'progresso_adm.html', {'mensagem_erro': mensagem_erro, 'progressos': progressos})

def exibir_metas(request):
    mensagem_erro = None
    metas = None

    if request.method == 'POST':
        nome_aluno = request.POST.get('nome_aluno')

        if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
            aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
            metas = Metas.objects.filter(aluno=aluno)
            if not metas:
                mensagem_erro = "Este usuário não possui nenhuma meta registrada."
        else:
            mensagem_erro = "Usuário não cadastrado ou não é usuário."

    return render(request, 'metas_adm.html', {'mensagem_erro': mensagem_erro, 'metas': metas})

def exibir_informacoes(request):
    if request.method == 'POST':
        nome_desejado = request.POST.get('nome_aluno', None)

        if nome_desejado:
           
            feedbacks = Feedback.objects.filter(aluno__nome=nome_desejado)

            
            progressos = Progresso.objects.filter(nome_aluno__nome=nome_desejado)

            if not feedbacks.exists() and not progressos.exists():
                mensagem = f"O aluno '{nome_desejado}' não possui feedbacks nem progresso registrados."
            else:
                mensagem = None

            context = {
                'feedbacks': feedbacks,
                'progressos': progressos,
                'mensagem': mensagem
            }
            return render(request, 'exibir_informacoes.html', context)
        else:
            mensagem = "Por favor, insira um nome de aluno válido."
    else:
        mensagem = None

    return render(request, 'form_busca_aluno.html', {'mensagem': mensagem})

def exibir_duvidas(request):
    mensagem_erro = ""
    duvidas = None
    nome_treinador = ""

    if request.method == 'GET' and 'nome_treinador' in request.GET:
        nome_treinador = request.GET.get('nome_treinador')
        try:
            treinador = Dados.objects.get(nome=nome_treinador, tipo='administrador')
            duvidas = Duvida.objects.filter(nome_treinador=treinador)
            if not duvidas:
                mensagem_erro = "Não há dúvidas registradas para este treinador."
        except Dados.DoesNotExist:
            mensagem_erro = "Treinador não encontrado no banco de dados."
        except Exception as e:
            mensagem_erro = str(e)
    
    return render(request, 'duvidas_adm.html', {'duvidas': duvidas, 'nome_treinador': nome_treinador, 'mensagem_erro': mensagem_erro})





