from django.db import models

class Dados(models.Model):
    # Definindo as opções para o campo 'tipo'
    TIPO_USUARIO_CHOICES = (
        ('administrador', 'Administrador'),
        ('usuario', 'Usuário'),
    )

    class Dados(models.Model):
        tipo = models.CharField(max_length=100)
        usuario = models.CharField(max_length=100)
        senha = models.CharField(max_length=100)
    
    def __str__(self):
        # Método para retornar uma string representativa do objeto
        return f"Tipo: {self.tipo} - Nome do usuário: {self.usuario} - Senha: {self.senha}"