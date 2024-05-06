from django import forms
from .models import Feedback
from .models import ProgressoAluno

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['aluno', 'feedback']


class ProgressoForm(forms.ModelForm):
    class Meta:
        model = ProgressoAluno
        fields = ['nome_aluno', 'metrica', 'data', 'progresso_observado']

