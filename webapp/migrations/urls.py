from django.urls import path
from . import views

urlpatterns = [
    path('pagina_login/', views.pagina_login, name="pagina_login")
    
    path('pagina_dicas/', views.pagina_dicas, name="pagina_dicas")
]
