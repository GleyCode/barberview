"""
URLs principais do projeto.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui todas as URLs do app 'barbearia'
    path('', include('barbearia.urls')),
]
