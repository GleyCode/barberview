"""
Models da aplicação Biblioteca.

Aqui definimos as tabelas do banco de dados usando classes Python.
Cada classe = uma tabela. Cada atributo = uma coluna.
"""

from django.db import models


class Agendamento(models.Model):
    """Representa um agendamento de serviço."""

    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        related_name='agendamentos'
    )    
    profissional = models.ForeignKey(
        'Profissional',
        on_delete=models.CASCADE,
        verbose_name='Profissional',
        related_name='agendamentos'
    )
    servico = models.ForeignKey(
        'Servico', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        verbose_name='Serviço',
        related_name='agendamentos'
    )
    data_agendamento = models.DateField(
        verbose_name='Data do agendamento'
    )
    hora_agendamento = models.TimeField(
        verbose_name='Hora do agendamento'
    )
    obs = models.TextField(
        blank=True,
        verbose_name='Observações adicionais'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('AGENDADO', 'Agendado'),
            ('FINALIZADO', 'Finalizado'),
            ('CANCELADO', 'Cancelado'),
        ],
        default='AGENDADO',
        verbose_name='Status do agendamento'
    )
   

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data_agendamento']    # Ordena pela data do agendamento

    def __str__(self):
        """Define como o objeto aparece."""
        return f'{self.cliente} - {self.data_agendamento.strftime("%d/%m/%Y %H:%M")} - {self.status}'


class Cliente(models.Model):
    """Representa o cliente da barbearia."""

    nome = models.CharField(
        max_length=200, 
        verbose_name='Nome completo'
    )
    cpf = models.CharField(
        max_length=14, 
        unique=True, 
        verbose_name='CPF'
    )
    telefone = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name='Telefone'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de cadastro'
    )
    obs = models.TextField(
        blank=True,
        verbose_name='Observações adicionais'
    )
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['data_cadastro']  # Ordena pela data de cadastro.

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    """Representa um profissional da barbearia."""

    nome = models.CharField(
        max_length=200, 
        verbose_name='Nome completo'
    )
    cpf = models.CharField(
        max_length=14, 
        unique=True, 
        verbose_name='CPF'
    )
    telefone = models.CharField(
        max_length=20, 
        blank=True, 
        verbose_name='Telefone'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de cadastro'
    )
    obs = models.TextField(
        blank=True,
        verbose_name='Observações adicionais'
    )
    

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    """Representa um serviço oferecido pela barbearia."""

    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do serviço'
    )
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço do serviço'
    )
    descricao = models.TextField(
        blank=True,
        verbose_name='Descrição do serviço'
    )


    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    def total_agendamentos(self):
        """Retorna o total de agendamentos para este serviço."""
        return self.agendamentos.count()
