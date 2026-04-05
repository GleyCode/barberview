# 📚 Minha Biblioteca — Projeto Django para Estudos

Um projeto Django completo para praticar os conceitos do tutorial oficial.

---

## 🗂️ Estrutura do Projeto

```
biblioteca_django/
│
├── manage.py                    # Comando principal do Django
├── setup.sh                     # Script de instalação rápida
│
├── minha_biblioteca/            # Pacote de configuração do projeto
│   ├── settings.py              # Todas as configurações
│   ├── urls.py                  # URLs raiz (aponta para o app)
│   └── wsgi.py                  # Servidor web
│
└── biblioteca/                  # Nossa aplicação
    ├── models.py                # 🗄️  Tabelas do banco (Livro, Autor, Categoria)
    ├── views.py                 # 👁️  Lógica de cada página
    ├── urls.py                  # 🔗  Mapeamento URL → View
    ├── forms.py                 # 📝  Formulários
    ├── admin.py                 # ⚙️  Configuração do painel admin
    ├── apps.py                  # 📋  Configuração do app
    │
    ├── management/
    │   └── commands/
    │       └── popular_banco.py # Comando para criar dados de exemplo
    │
    └── templates/
        └── biblioteca/
            ├── base.html                    # Template pai (navbar, layout)
            ├── livro_lista.html             # Lista de livros + busca
            ├── livro_detalhe.html           # Detalhes de um livro
            ├── livro_form.html              # Formulário criar/editar livro
            ├── livro_confirmar_delete.html  # Confirmação de exclusão
            ├── autor_lista.html             # Lista de autores
            ├── autor_detalhe.html           # Detalhes do autor + seus livros
            ├── autor_form.html              # Formulário criar/editar autor
            ├── categoria_lista.html         # Lista de categorias
            └── categoria_form.html          # Formulário criar categoria
```

---

## 🚀 Como rodar o projeto

### Opção 1 — Script automático
```bash
bash setup.sh
```

### Opção 2 — Passo a passo manual

```bash
# 1. Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 2. Instalar o Django
pip install django

# 3. Criar o banco de dados
python manage.py migrate

# 4. Popular com dados de exemplo
python manage.py popular_banco

# 5. Criar usuário para o Admin (opcional)
python manage.py createsuperuser

# 6. Iniciar o servidor
python manage.py runserver
```

Acesse: **http://localhost:8000**
Admin: **http://localhost:8000/admin**

---

## 📖 O que o projeto tem

| Recurso | Descrição |
|---|---|
| **3 Models** | `Livro`, `Autor`, `Categoria` com relações ForeignKey e ManyToMany |
| **CRUD completo** | Criar, Listar, Detalhar, Editar e Deletar livros e autores |
| **Busca** | Filtro por título ou nome do autor |
| **Django Admin** | Interface automática configurada |
| **Formulários** | Validação automática via `ModelForm` |
| **Mensagens** | Feedback de sucesso após cada ação |
| **Herança de template** | `base.html` com `{% block %}` |
| **Comando customizado** | `popular_banco` para criar dados de exemplo |

---

## 🏋️ Exercícios para praticar

Tente implementar estas funcionalidades para treinar:

### Nível Iniciante
- [ ] Adicionar um campo `editora` ao model `Livro`
- [ ] Criar uma página de "sobre" (`/sobre/`) com informações estáticas
- [ ] Mostrar a data de cadastro formatada no detalhe do livro
- [ ] Adicionar um filtro por status (disponível/emprestado) na lista

### Nível Intermediário
- [ ] Adicionar paginação na lista de livros (use `Paginator`)
- [ ] Criar a funcionalidade de deletar autor (cuidado com livros relacionados!)
- [ ] Adicionar uma página de busca avançada (filtrar por categoria, ano, status)
- [ ] Exibir os livros de uma categoria clicando nela

### Nível Avançado
- [ ] Adicionar sistema de login (só usuários logados podem criar/editar/deletar)
- [ ] Criar uma API simples retornando JSON com `JsonResponse`
- [ ] Adicionar upload de capa do livro com `ImageField`
- [ ] Criar testes automatizados com `TestCase`

---

## 🧠 Conceitos Django usados neste projeto

| Arquivo | Conceito |
|---|---|
| `models.py` | `CharField`, `TextField`, `ForeignKey`, `ManyToManyField`, `Meta`, `__str__` |
| `views.py` | `render`, `redirect`, `get_object_or_404`, `request.method`, `Q objects` |
| `forms.py` | `ModelForm`, `widgets`, `cleaned_data` |
| `urls.py` | `path`, `include`, `<int:pk>`, `name=` |
| `admin.py` | `@admin.register`, `list_display`, `search_fields`, `list_filter` |
| `templates/` | `{% extends %}`, `{% block %}`, `{% for %}`, `{% if %}`, `{% url %}`, `{{ variavel\|filtro }}` |
| `management/` | `BaseCommand`, `handle`, `get_or_create` |
