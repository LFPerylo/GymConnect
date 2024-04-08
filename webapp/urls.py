from django.urls import path
from . import views

urlpatterns = [
    path('pagina_login/', views.pagina_login, name="pagina_login"),
    
    path('pagina_dicas/', views.pagina_dicas, name="pagina_dicas"),

    path('pagina_home/', views.pagina_home, name="pagina_home"),

    path('pagina_treinospredefinidos/', views.pagina_treinospredefinidos, name="pagina_treinospredefinidos"),

    path('pagina_duvidas/', views.pagina_duvidas, name="pagina_duvidas")
]
