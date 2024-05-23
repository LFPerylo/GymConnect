from django import forms
from .models import Feedback
from .models import Progresso
from .models import Dados, Dica,Consulta,TreinoPredefinido,Duvida,Treino

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
    nome_aluno = forms.ModelChoiceField(queryset=Dados.objects.filter(tipo='usuario'))

    class Meta:
        model = Treino
        fields = '__all__'

class DuvidaForm(forms.Form):
    nome_treinador = forms.CharField(max_length=100, label="Nome do Professor")
    duvida_escrita = forms.CharField(widget=forms.Textarea, label="Dúvida")
       

