
from django.contrib import admin
from django.urls import path, include
from webapp import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('home_aluno/', views.home_aluno, name="home_aluno"),
    path('home_adm/', views.home_adm, name="home_adm"),

    path('treinospredefinidos/', views.treinospredefinidos, name="treinospredefinidos"),
    path('treinospredefinidos_adm/', views.treinospredefinidos_adm, name="treinospredefinidos_adm"),
    path('criar_treino_predefinido/', views.criar_treino_predefinido, name="criar_treino_predefinido"),
    path('exibir_treino_predefinido/', views.exibir_treino_predefinido, name="exibir_treino_predefinido"),
    
    path('marcar_consulta/',views.marcar_consulta, name="marcar_consulta"),
    path('agendar_consulta/',views.agendar_consulta, name="agendar_consulta"),
    
    path('enviar_feedback/', views.enviar_feedback, name="enviar_feedback"),
    path('feedback/',views.feedback, name="feedback"),
    
    path('enviar_duvida/', views.enviar_duvida, name='enviar_duvida'),
    path('duvidas/', views.duvidas, name="duvidas"),
    
    path('adicionar_dica/', views.adicionar_dica, name='adicionar_dica'),
    path('exibir_dica/', views.exibir_dica, name='exibir_dica'),
    path('dicas_adm/', views.dicas_adm, name="dicas_adm"),
    path('dicas/', views.dicas, name="dicas"),
    
    path('progresso/', views.progresso, name='progresso'),
    path('registrar_progresso/', views.registrar_progresso, name="registrar_progresso"),
    
    path('admin/', admin.site.urls),
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('fazer_login/', views.fazer_login, name="fazer_login"),
    path('cadastro/',views.cadastro, name="cadastro"),
    path('', views.login, name="login"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
