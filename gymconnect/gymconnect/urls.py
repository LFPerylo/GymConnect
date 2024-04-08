from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls'))
]
