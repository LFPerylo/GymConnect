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
        return f"{self.nome}"
    
class Feedback(models.Model):
    aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=100)

    def __str__(self):
        return f"Feedback de {self.aluno.nome}"

class ProgressoAluno(models.Model):
    progresso_observado = models.TextField()
    metrica = models.CharField(max_length=100)
    data = models.DateField()
    nome_aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)

    def __str__(self):
        return f"Progresso de {self.nome_aluno.nome} em {self.metrica} em {self.data}"

class Duvida(models.Model):
    duvida_escrita = models.TextField()
    nome_treinador = models.CharField(max_length=100)

    def __str__(self):
        return self.duvida_escrita

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

class TreinoPredefinido(models.Model):
    TIPO_CHOICES = (
        ('costas', 'Costas'),
        ('peito', 'Peito'),
        ('perna', 'Perna'),
        ('braco', 'Braço'),
    )
    tipo_treino = models.CharField(max_length=20, choices=TIPO_CHOICES)
    exercicio1_nome = models.CharField(max_length=100)
    exercicio1_series = models.PositiveIntegerField()
    exercicio1_repeticoes = models.PositiveIntegerField()
    exercicio2_nome = models.CharField(max_length=100)
    exercicio2_series = models.PositiveIntegerField()
    exercicio2_repeticoes = models.PositiveIntegerField()
    exercicio3_nome = models.CharField(max_length=100)
    exercicio3_series = models.PositiveIntegerField()
    exercicio3_repeticoes = models.PositiveIntegerField()
    exercicio4_nome = models.CharField(max_length=100)
    exercicio4_series = models.PositiveIntegerField()
    exercicio4_repeticoes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_tipo_treino_display()} - {self.exercicio1_nome}, {self.exercicio2_nome}, {self.exercicio3_nome}, {self.exercicio4_nome}"
