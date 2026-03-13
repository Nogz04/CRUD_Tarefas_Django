# 📝 Gerenciador de Tarefas Django

Bem-vindo ao projeto **Gerenciador de Tarefas**! Este é um sistema simples de CRUD utilizando Python Django, onde o usuário pode adicionar, visualizar, editar e remover suas tarefas.

---

## 🚀 Funcionalidades

- **✨ Interface**: Design moderno e limp.
- **📋 Listagem de Tarefas**: Visualize todas as suas tarefas em uma tabela organizada.
- **➕ Cadastro de Tarefas**: Adicione novas tarefas com nome e descrição.
- **✏️ Edição de tarefas**: Atualize informações de tarefas existentes de forma intuitiva.
- **🗑️ Remoção de tarefas**: Exclua tarefas que não são mais necessárias.
- **🏷️ Status Visual**: Badges coloridos para identificar tarefas Pendentes e Concluídas.

---

## 🏗️ Organização do Projeto

A estrutura de pastas foi organizada seguindo as melhores práticas do Django:

```text
d:\Python Django\
├── 📂 tarefas\              # Aplicação principal (Lógica de tarefas)
│   ├── 📂 migrations\       # Histórico do Banco de Dados
│   ├── 📂 static\           # Arquivos estáticos (CSS, JS, Imagens)
│   │   └── 📂 tarefas\
│   │       └── 📂 css\
│   │           └── style.css # Estilo premium customizado
│   ├── 📂 templates\        # Arquivos HTML da aplicação
│   │   └── 📂 tarefas\
│   │       ├── cadastrar_tarefa.html
│   │       ├── editar_tarefa.html
│   │       └── home.html
│   ├── admin.py             # Configuração do painel administrativo
│   ├── forms.py             # Definição dos formulários Django
│   ├── models.py            # Estrutura do Banco de Dados
│   ├── urls.py              # Rotas específicas da aplicação
│   └── views.py             # Lógica de processamento das páginas
├── 📂 projeto1\             # Configurações globais do projeto (Settings/URLs)
├── 📂 venv\                 # Ambiente virtual 
├── .gitignore               # Regras de arquivos ignorados pelo Git
├── db.sqlite3               # Banco de dados local (SQLite)
├── manage.py                # Utilitário de comando do Django
└── README.md                # Esta documentação
```

---

## 🛠️ Tecnologias Utilizadas

- **🐍 Python**: Linguagem de programação principal.
- **🎸 Django 6.0**: Framework web.
- **🎨 HTML5 e CSS3**: Utilizado para criação do frontend e estilização do mesmo.
- **🗄️ SQLite**: Banco de dados leve e eficiente para desenvolvimento.
- **🖋️ Google Fonts**: Tipografia moderna e legível.

---

## 🔗 Endpoints da Aplicação

Para acessar as funcionalidades do sistema, utilize as seguintes rotas:

- **Menu Principal**: ` `
- **Cadastrar Tarefa**: `cadastrar/`
- **Editar Tarefa**: `editar/<id>/`
- **Remover Tarefa**: `remover/<id>/`

---

## ⚙️ Como Executar o Projeto

1. **Ativar o Ambiente Virtual:**
   ```powershell
   .\venv\Scripts\activate
   ```

2. **Migrar o Banco de Dados (se necessário):**
   ```powershell
   python manage.py migrate
   ```

3. **Iniciar o Servidor:**
   ```powershell
   python manage.py runserver
   ```

4. **Acesse no Navegador:**
   O Django iniciará por padrão em `http://127.0.0.1:8000/` na tela home. (esse sistema é apenas local)

---

## 🎨 Design System

O projeto utiliza um sistema de cores harmônico definido em variáveis CSS:
- **Primary**: Blue (#3b82f6) - Ações principais.
- **Success**: Emerald (#10b981) - Cadastros e conclusões.
- **Danger**: Rose (#ef4444) - Remoções e exclusões.
- **Background**: Slate (#f8fafc) - Ambiente visual limpo.

---

## ✍️ Matheus Nogueira
