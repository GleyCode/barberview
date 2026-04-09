"""
Formulários da aplicação BarberView.

ModelForm gera o formulário automaticamente a partir do Model.
"""

from django import forms
from .models import Agendamento, Cliente, Profissional, Servico


class AgendamentoForm(forms.ModelForm):
    """Formulário para criar/editar Agendamento."""

    class Meta:
        model = Agendamento
        fields = ['cliente', 'profissional', 'status', 'servico', 'data_agendamento', 'hora_agendamento', 'obs']
        widgets = {
            # Personaliza como cada campo é renderizado no HTML
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'profissional': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'servico': forms.Select(attrs={'class': 'form-select'}),
            'data_agendamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_agendamento': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O cliente prefere...', 'rows': 3}),
        }


class ClienteForm(forms.ModelForm):
    """Formulário para criar/editar Cliente."""

    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'obs']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João da Silva Vargas'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (85) 11111-1111'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O cliente prefere...', 'rows': 3}),
        }


class ProfissionalForm(forms.ModelForm):
    """Formulário para criar/editar Profissional."""

    class Meta:
        model = Profissional
        fields = ['nome', 'cpf', 'telefone', 'obs']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João da Silva Vargas'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (85) 11111-1111'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'O profissional é ...', 'rows': 5}),
        }


class ServicoForm(forms.ModelForm):
    """Formulário para criar/editar Serviço."""

    class Meta:
        model = Servico
        fields = ['nome', 'preco', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do serviço'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço do serviço'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do serviço', 'rows': 3}),
        }
        
        
class BuscaForm(forms.Form):
    """Formulário simples de busca."""

    q = forms.CharField(
        label='Buscar',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Busque por cliente ou profissional',
        }),
    )
