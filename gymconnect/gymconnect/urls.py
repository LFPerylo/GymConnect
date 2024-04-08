from django.contrib import admin
from django.urls import path,include
from webapp.migrations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls'))
]
