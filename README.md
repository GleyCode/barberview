# 💈 BarberWeb

> Interface web para sistema de gestão de barbearias, construída com Django, HTML e Bootstrap 5.

---

## 📋 Sobre o Projeto

O **BarberWeb** é uma aplicação web desenvolvida com Django que oferece uma interface completa para a gestão de barbearias. Com foco em usabilidade e organização, o sistema permite administrar os principais recursos de uma barbearia de forma simples e eficiente.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| **Python** | 3.x | Back-end e lógica de negócio |
| **Django** | — | Framework web principal |
| **HTML5** | — | Estrutura das páginas (55% do projeto) |
| **Bootstrap 5** | — | Estilização e responsividade |
| **SQLite** | — | Banco de dados padrão |

---

## 🗂️ Estrutura do Projeto

```
barberview/
│
├── manage.py                  # Ponto de entrada do Django
├── db.sqlite3                 # Banco de dados SQLite
│
├── barbearia_project/         # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── barbearia/                 # Aplicação principal
    ├── models.py              # Modelos de dados
    ├── views.py               # Lógica das páginas
    ├── urls.py                # Rotas da aplicação
    ├── forms.py               # Formulários
    ├── admin.py               # Configuração do painel admin
    └── templates/             # Templates HTML
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado
- Git instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/GleyCode/barberview.git
cd barberview

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Instale as dependências
pip install django

# 4. Execute as migrações do banco de dados
python manage.py migrate

# 5. (Opcional) Crie um superusuário para acessar o Admin
python manage.py createsuperuser

# 6. Inicie o servidor de desenvolvimento
python manage.py runserver
```

Acesse a aplicação em: **http://localhost:8000**

Painel administrativo: **http://localhost:8000/admin**

---

## ✨ Funcionalidades

- 📋 Cadastro e gerenciamento de dados da barbearia
- 👤 Painel administrativo Django integrado
- 📱 Interface responsiva com Bootstrap 5
- 🗄️ Persistência de dados com SQLite

---

## 👤 Autor

Feito por **[GleyCode](https://github.com/GleyCode)** 🚀

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
