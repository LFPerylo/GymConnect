from django.db import models
from django.contrib.auth.models import User



class Dados(models.Model):
    # Definindo as opções para o campo 'tipo'
    TIPO_USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuário'),
    )

    tipo = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, default='usuario')
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        # Método para retornar uma string representativa do objeto
        return f"Tipo: {self.tipo} - Nome do usuário: {self.nome} - Senha: {self.senha}"
    
class Feedback(models.Model):
    aluno = models.CharField(max_length=50)
    feedback = models.TextField(max_length=100)

    def __str__(self):
        return f"Feedback de {self.aluno}"
    
class Progresso(models.Model):
    nome_aluno = models.CharField(max_length=100)
    metrica = models.CharField(max_length=100)
    data = models.DateField()
    progresso_observado = models.TextField()

    def __str__(self):
        return f"Progresso de {self.nome_aluno} em {self.metrica} em {self.data}"

class ProgressoAluno(models.Model):
    progresso_observado = models.TextField()
    metrica = models.CharField(max_length=100)
    data = models.DateField()
    nome_aluno = models.CharField(max_length=100)

class Duvida(models.Model):
    duvida_escrita = models.TextField()
    nome_treinador = models.CharField(max_length=100)

    def __str__(self):
        return self.duvida_escrita

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Feedback(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback para {self.aluno}"

class Consulta(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    mensagem = models.TextField(blank=True)  # O campo mensagem é opcional

    def __str__(self):
        return f"Consulta em {self.data} às {self.horario}"

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagens/')

class Dica(models.Model):
    TIPO_DICA_CHOICES = (
        ('nutricao', 'Nutrição'),
        ('treino', 'Treino'),
        ('cardio', 'Cardio'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_DICA_CHOICES)
    texto = models.TextField()

    def __str__(self):
        return self.texto