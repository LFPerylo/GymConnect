
from django.urls import path,include
from webapp import views

urlpatterns = [
    path('', views.login, name="login"),
    
    path('', views.dicas, name="dicas"),

    path('', views.home, name="home"),

    path('', views.treinospredefinidos, name="treinospredefinidos"),

    path('', views.duvidas, name="duvidas")
]
