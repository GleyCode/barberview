"""
Configuração do Django Admin.

O admin é uma interface automática para gerenciar os dados.
Acesse em: http://localhost:8000/admin/
"""

from django.contrib import admin
from .models import Agendamento, Cliente, Profissional, Servico


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'profissional', 'status']
    list_filter = ['status']  # Filtro lateral
    search_fields = ['cliente__nome', 'profissional__nome']  # Campo de busca


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone']
    search_fields = ['nome', 'cpf']


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone']
    search_fields = ['nome', 'cpf']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'descricao']
    search_fields = ['nome']
