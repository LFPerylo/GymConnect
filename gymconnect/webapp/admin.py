
from django.contrib import admin
from .models import Dados, ProgressoAluno, Feedback, Duvida,Feedback, Consulta, Imagem,Dica,TreinoPredefinido

admin.site.register(Dados)
admin.site.register(ProgressoAluno)
admin.site.register(Feedback)
admin.site.register(Duvida)
admin.site.register(Consulta)
admin.site.register(Imagem)
admin.site.register(Dica)
admin.site.register(TreinoPredefinido)