from django import forms
from .models import Feedback
from .models import ProgressoAluno
from .models import Dados, Dica,Consulta,TreinoPredefinido

class FeedbackForm(forms.ModelForm):
    nome_aluno = forms.CharField(max_length=50)
    feedback = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ['nome_aluno', 'feedback']

class ProgressoForm(forms.ModelForm):
    class Meta:
        model = ProgressoAluno
        fields = ['progresso_observado', 'metrica', 'data', 'nome_aluno']

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

