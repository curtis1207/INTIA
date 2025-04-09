from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')),  # on inclut les routes de l'app gestion
]

print("👉 URLs de gestion chargées")