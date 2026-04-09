"""
Views da aplicação Barbearia.

Views recebem uma requisição HTTP e retornam uma resposta.
Aqui usamos views baseadas em funções (FBV), que são mais simples de entender.
"""

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q  # Para fazer buscas com OR

from .models import Agendamento, Cliente, Profissional, Servico
from .forms import AgendamentoForm, ClienteForm, ProfissionalForm, ServicoForm, BuscaForm


# =============================================================================
# VIEWS DE AGENDAMENTOS
# =============================================================================

def agendamento_lista(request):
    """Lista todos os agendamentos com opção de busca."""
    form = BuscaForm(request.GET)  # GET porque a busca vem pela URL (?q=...)
    agendamentos = Agendamento.objects.select_related('cliente', 'profissional')  # Otimização: carrega os relacionamentos junto

    # Se o formulário foi preenchido e é válido
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            # Q permite fazer OR: busca no título OU no nome do autor
            agendamentos = agendamentos.filter(
                Q(cliente__nome__icontains=q) |
                Q(profissional__nome__icontains=q)
            )

    # Paginação: mostra 3 clientes por página.
    paginator = Paginator(agendamentos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'barbearia/agendamento/agendamento_lista.html', context)


def agendamento_detalhe(request, pk):
    """Mostra os detalhes de um agendamento específico."""
    # get_object_or_404 retorna o objeto ou uma página de erro 404
    agendamento = get_object_or_404(Agendamento, pk=pk)
    context = {
        'agendamento': agendamento,
    }
    return render(request, 'barbearia/agendamento/agendamento_detalhe.html', context)


def agendamento_criar(request):
    """Cria um novo agendamento."""
    if request.method == 'POST':
        # O usuário enviou o formulário
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save()  # Salva no banco de dados
            messages.success(request, f'Agendamento para "{agendamento.cliente.nome}" cadastrado com sucesso!')
            return redirect('agendamento_detalhe', pk=agendamento.pk)
    else:
        # O usuário está acessando a página pela primeira vez (GET)
        form = AgendamentoForm()
    context = {
        'form': form,
        'finalidade': 'Cadastrar',
    }
    return render(request, 'barbearia/agendamento/agendamento_form.html', context)


def agendamento_editar(request, pk):
    """Edita um agendamento existente."""
    agendamento = get_object_or_404(Agendamento, pk=pk)

    if request.method == 'POST':
        # instance=agendamento diz ao form que deve ATUALIZAR, não criar um novo
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, f'Agendamento para "{agendamento.cliente.nome}" atualizado!')
            return redirect('agendamento_detalhe', pk=agendamento.pk)
    else: # GET
        form = AgendamentoForm(instance=agendamento)  # Preenche o form com os dados existentes
    context = {
        'form': form,
        'acao': 'Editar',
        'agendamento': agendamento,
    }
    return render(request, 'barbearia/agendamento/agendamento_form.html', context)


def agendamento_deletar(request, pk):
    """Deleta um agendamento."""
    agendamento = get_object_or_404(Agendamento, pk=pk)

    if request.method == 'POST':
        cliente_nome = agendamento.cliente.nome
        agendamento.delete()
        messages.success(request, f'Agendamento para "{cliente_nome}" removido!')
        return redirect('agendamento_lista')
    context = {
        'agendamento': agendamento,
    }
    # GET: mostra página de confirmação antes de deletar
    return render(request, 'barbearia/agendamento/agendamento_confirmar_delete.html', context)

# =============================================================================
# VIEWS DE CLIENTES
# =============================================================================

def cliente_lista(request):
    """Lista todos os clientes."""
    form = BuscaForm(request.GET)
    clientes = Cliente.objects.all()
    
    # Se o formulário foi preenchido e é válido
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            clientes = clientes.filter(nome__icontains=q)
    
    # Paginação: mostra 10 clientes por página.
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'barbearia/cliente/cliente_lista.html', context)


def cliente_detalhe(request, pk):
    """Mostra detalhes de um cliente específico."""
    cliente = get_object_or_404(Cliente, pk=pk)
    
    context = {
        'cliente': cliente,    
    }
    
    return render(request, 'barbearia/cliente/cliente_detalhe.html', context)


def cliente_criar(request):
    """Cria um novo cliente."""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente "{cliente.nome}" cadastrado!')
            return redirect('cliente_detalhe', pk=cliente.pk)
    else:
        form = ClienteForm()
        
    context = {
        'form': form,
        'finalidade': 'Cadastrar',
    }
    
    return render(request, 'barbearia/cliente/cliente_form.html', context)


def cliente_editar(request, pk):
    """Edita um cliente existente."""
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente "{cliente.nome}" atualizado!')
            return redirect('cliente_detalhe', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'acao': 'Editar',
        'cliente': cliente,
    }
    
    return render(request, 'barbearia/cliente/cliente_form.html', context)


# =============================================================================
# VIEWS DE PROFISSIONAIS
# =============================================================================

def profissional_lista(request):
    """Lista todos os profissionais."""
    form = BuscaForm(request.GET)
    profissionais = Profissional.objects.all()
    
    # Se o formulário foi preenchido e é válido
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            profissionais = profissionais.filter(nome__icontains=q)

    # Paginação: mostra 6 profissionais por página.
    paginator = Paginator(profissionais, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'barbearia/profissional/profissional_lista.html', context)


def profissional_detalhe(request, pk):
    """Mostra detalhes de um profissional específico."""
    profissional = get_object_or_404(Profissional, pk=pk)
    
    context = {
        'profissional': profissional,
    }
    
    return render(request, 'barbearia/profissional/profissional_detalhe.html', context)


def profissional_criar(request):
    """Cria um novo profissional."""
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            profissional = form.save()
            messages.success(request, f'Profissional "{profissional.nome}" cadastrado!')
            return redirect('profissional_detalhe', pk=profissional.pk)
    else:
        form = ProfissionalForm()
        
    context = {
        'form': form,
        'finalidade': 'Cadastrar',
    }
    
    return render(request, 'barbearia/profissional/profissional_form.html', context)


def profissional_editar(request, pk):
    """Edita um profissional existente."""
    profissional = get_object_or_404(Profissional, pk=pk)

    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profissional "{profissional.nome}" atualizado!')
            return redirect('profissional_detalhe', pk=profissional.pk)
    else:
        form = ProfissionalForm(instance=profissional)

    context = {
        'form': form,
        'acao': 'Editar',
        'profissional': profissional,
    }
    
    return render(request, 'barbearia/profissional/profissional_form.html', context)


# =============================================================================
# VIEWS DE SERVIÇOS
# =============================================================================

def servico_lista(request):
    """Lista todos os serviços."""
    servicos = Servico.objects.all()
    
    context = {
        'servicos': servicos,
    }
    
    return render(request, 'barbearia/servico/servico_lista.html', context)


def servico_detalhe(request, pk):
    """Mostra detalhes de um serviço específico."""
    servico = get_object_or_404(Servico, pk=pk)
    
    context = {
        'servico': servico,
    }
    
    return render(request, 'barbearia/servico/servico_detalhe.html', context)


def servico_criar(request):
    """Cria um novo serviço."""
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save()
            messages.success(request, f'Serviço "{servico.nome}" cadastrado!')
            return redirect('servico_detalhe', pk=servico.pk)
    else:
        form = ServicoForm()

    context = {
        'form': form,
        'acao': 'Cadastrar',
    }
    
    return render(request, 'barbearia/servico/servico_form.html', context)


def servico_editar(request, pk):
    """Edita um serviço existente."""
    servico = get_object_or_404(Servico, pk=pk)

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, f'Serviço "{servico.nome}" atualizado!')
            return redirect('servico_detalhe', pk=servico.pk)
    else:
        form = ServicoForm(instance=servico)

    context = {
        'form': form,
        'acao': 'Editar',
        'servico': servico,
    }
    
    return render(request, 'barbearia/servico/servico_form.html', context)
