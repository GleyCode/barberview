"""
URLs da aplicação Biblioteca.

Cada path() mapeia uma URL para uma view.
O 'name' permite referenciar a URL nos templates com {% url 'name' %}
"""

from django.urls import path
from . import views

#app_name = 'barbearia'
urlpatterns = [
    # Página inicial = lista de agendamentos
    path('', views.agendamento_lista, name='agendamento_lista'),

    # URLs de Agendamentos
    path('agendamentos/<int:pk>/', views.agendamento_detalhe, name='agendamento_detalhe'),
    path('agendamentos/novo/', views.agendamento_criar, name='agendamento_criar'),
    path('agendamentos/<int:pk>/editar/', views.agendamento_editar, name='agendamento_editar'),
    path('agendamentos/<int:pk>/deletar/', views.agendamento_deletar, name='agendamento_deletar'),

    # URLs de Clientes
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/<int:pk>/', views.cliente_detalhe, name='cliente_detalhe'),
    path('clientes/novo/', views.cliente_criar, name='cliente_criar'),
    path('clientes/<int:pk>/editar/', views.cliente_editar, name='cliente_editar'),

    # URLs de Profissionais
    path('profissionais/', views.profissional_lista, name='profissional_lista'),
    path('profissionais/<int:pk>/', views.profissional_detalhe, name='profissional_detalhe'),
    path('profissionais/novo/', views.profissional_criar, name='profissional_criar'),
    path('profissionais/<int:pk>/editar/', views.profissional_editar, name='profissional_editar'),
    
    # URLs de Serviços
    path('servicos/', views.servico_lista, name='servico_lista'),
    path('servicos/<int:pk>/', views.servico_detalhe, name='servico_detalhe'),
    path('servicos/novo/', views.servico_criar, name='servico_criar'),
    path('servicos/<int:pk>/editar/', views.servico_editar, name='servico_editar'),
]
