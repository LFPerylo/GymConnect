
from django.urls import path,include
from webapp import views

urlpatterns = [
    path('', views.login, name="login"),
    
    path('dicas.html', views.dicas, name="dicas"),

    path('home.html', views.home, name="home"),

    path('treinospredefinidos.html', views.treinospredefinidos, name="treinospredefinidos"),

    path('duvidas.html', views.duvidas, name="duvidas")
]
