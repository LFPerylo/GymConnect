
from django.urls import path
from django.contrib import admin
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login, name="login"),
    
    path('home/', views.home, name="home"),
    
    path('dicas/', views.dicas, name="dicas"),

    path('treino/', views.treinospredefinidos, name="treinospredefinidos"),

    path('duvidas/', views.duvidas, name="duvidas")
]
