
from django.contrib import admin
from django.urls import path, include
from webapp import views  # Garanta que suas views estão corretamente importadas deste módulo
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.login, name="login"),
    path('dicas/', views.dicas, name="dicas"),
    path('home_aluno/', views.home_aluno, name="homealuno"),
    path('home_adm/', views.home_adm, name="homeadm"),
    path('treinospredefinidos/', views.treinospredefinidos, name="treinospredefinidos"),
    path('duvidas/', views.duvidas, name="duvidas")
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
