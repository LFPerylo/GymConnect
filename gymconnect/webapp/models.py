from django.db import models
from django.contrib.auth.models import User



class Dados(models.Model):
    
    TIPO_USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuário'),
    )

    tipo = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES, default='usuario')
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        
        return f"{self.nome}"
    
class Feedback(models.Model):
    aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=100)

    def __str__(self):
        return f"Feedback de {self.aluno.nome}"

class Progresso(models.Model):
    TIPO_PROGRESSO_CHOICES = (
        ('forca', 'Força'),
        ('resistencia', 'Resistência'),
        ('circunferencia', 'Circunferência'),
    )
    tipo_progresso = models.CharField(max_length=100, choices=TIPO_PROGRESSO_CHOICES)
    data = models.DateField()
    nome_aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)  
    observacao = models.TextField()

    def __str__(self):
        return f"{self.nome_aluno} - {self.tipo_progresso} em {self.data}"

class Duvida(models.Model):
    nome_treinador = models.ForeignKey(Dados, on_delete=models.CASCADE)
    duvida_escrita = models.TextField()

    def __str__(self):
        return self.duvida_escrita

class Consulta(models.Model):
    
    data = models.DateField()
    horario = models.TimeField()
    mensagem = models.TextField(blank=True)  

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
    
class Treino(models.Model):
    TIPO_TREINO_CHOICES = (
        ('costas', 'Costas'),
        ('peito', 'Peito'),
        ('perna', 'Perna'),
        ('braco', 'Braço'),
    )

    aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)
    tipo_treino = models.CharField(max_length=100, choices=TIPO_TREINO_CHOICES)
    
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
        return f"Treino de {self.aluno.nome} - {self.get_tipo_treino_display()} - {self.exercicio1_nome}, {self.exercicio2_nome}, {self.exercicio3_nome}, {self.exercicio4_nome}"


class Metas(models.Model):
    TIPO_META_CHOICES = (
        ('perda de peso', 'Perda de Peso'),
        ('ganho de massa', 'Ganho de Massa'),
        ('melhoria de resistencia', 'Melhoria de Resistência'),
    )

    aluno = models.ForeignKey(Dados, on_delete=models.CASCADE)
    tipo_meta = models.CharField(max_length=50, choices=TIPO_META_CHOICES)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Meta de {self.aluno.nome} - {self.get_tipo_meta_display()}"
    
class Info(models.Model):
    professor = models.ForeignKey(Dados, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=50)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"Informações de {self.professor.nome}"