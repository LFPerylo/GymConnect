from django.urls import path # type: ignore
from . import views
from .views import agendar_consulta  # Certifique-se de importar a view corretamente

urlpatterns = [
    # Outras URLs do seu aplicativo, se houver
    path('agendar_consulta/', agendar_consulta, name='agendar_consulta'),
]
