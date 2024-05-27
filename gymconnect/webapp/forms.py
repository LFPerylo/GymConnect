from django import forms
from .models import Feedback
from .models import Progresso
from .models import Dados, Dica,Consulta,TreinoPredefinido,Duvida,Treino,Metas,Info

class FeedbackForm(forms.ModelForm):
    nome_aluno = forms.CharField(max_length=50)
    feedback = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ['nome_aluno', 'feedback']

class ProgressoForm(forms.Form):
    nome_aluno = forms.CharField(max_length=50)
    TIPO_PROGRESSO_CHOICES = (
        ('forca', 'Força'),
        ('resistencia', 'Resistência'),
        ('circunferencia', 'Circunferência'),
    )
    tipo_progresso = forms.ChoiceField(choices=TIPO_PROGRESSO_CHOICES)
    observacao = forms.CharField(widget=forms.Textarea)
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class LoginForm(forms.Form):
    nome = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
    tipo = forms.CharField(widget=forms.HiddenInput(), required=False)
    

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'senha', 'tipo']

class DicaForm(forms.ModelForm):
    class Meta:
        model = Dica
        fields = ['tipo', 'texto']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'horario', 'mensagem']

class TreinoPredefinidoForm(forms.ModelForm):
    class Meta:
        model = TreinoPredefinido
        fields = '__all__'


class TreinoForm(forms.ModelForm):
    nome_aluno = forms.CharField(max_length=100)

    class Meta:
        model = Treino
        fields = [
            'nome_aluno', 'tipo_treino', 
            'exercicio1_nome', 'exercicio1_series', 'exercicio1_repeticoes', 
            'exercicio2_nome', 'exercicio2_series', 'exercicio2_repeticoes', 
            'exercicio3_nome', 'exercicio3_series', 'exercicio3_repeticoes', 
            'exercicio4_nome', 'exercicio4_series', 'exercicio4_repeticoes'
        ]

class NomeAlunoForm(forms.Form):
    nome_aluno = forms.CharField(label='Nome do Aluno', max_length=100)

class TreinoEditForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['tipo_treino', 'exercicio1_nome', 'exercicio1_series', 'exercicio1_repeticoes', 
                  'exercicio2_nome', 'exercicio2_series', 'exercicio2_repeticoes',
                  'exercicio3_nome', 'exercicio3_series', 'exercicio3_repeticoes',
                  'exercicio4_nome', 'exercicio4_series', 'exercicio4_repeticoes']
        
class DuvidaForm(forms.Form):
    nome_treinador = forms.CharField(max_length=100, label="Nome do Professor")
    duvida_escrita = forms.CharField(widget=forms.Textarea, label="Dúvida")
       
class MetasForm(forms.ModelForm):
    nome_aluno = forms.CharField(max_length=100, label='Nome do Aluno')

    class Meta:
        model = Metas
        fields = ['nome_aluno', 'tipo_meta', 'observacoes']

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['professor', 'telefone', 'instagram', 'facebook', 'email']

