# API de Doação de Livros

Uma API RESTful desenvolvida com Flask e SQLite para gerenciar um sistema de doação de livros.

## 📋 Descrição

Esta aplicação permite cadastrar livros para doação, listar todos os livros cadastrados e fornece uma página inicial informativa. Foi construída seguindo princípios de modularização e separação de responsabilidades, utilizando o padrão Blueprint do Flask.

## 🔧 Tecnologias utilizadas

- **Python 3.x**
- **Flask**: Framework web leve para Python
- **SQLite**: Banco de dados relacional embutido
- **Blueprint**: Padrão de organização do Flask para melhor estruturação do código

## 📁 Estrutura do projeto

```
projeto-livros/
├── app/                      # Pasta principal da aplicação
│   ├── __init__.py           # Inicialização da aplicação Flask
│   ├── config.py             # Configurações da aplicação
│   ├── models/               # Modelos de dados
│   │   ├── __init__.py
│   │   └── livro.py          # Modelo de Livro
│   ├── routes/               # Rotas da API
│   │   ├── __init__.py
│   │   └── livros_routes.py  # Rotas para livros
│   └── database/             # Operações de banco de dados
│       ├── __init__.py
│       └── db.py             # Funções do banco de dados
├── instance/                 # Diretório para banco de dados SQLite
│   └── database.db
├── run.py                    # Script para executar a aplicação
├── requirements.txt          # Dependências do projeto
└── scripts/                  # Scripts utilitários
    └── populate_db.py        # Script para popular o banco
```

## 🚀 Como executar o projeto

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone este repositório:

   ```
   git clone https://github.com/seu-usuario/api-doacao-livros.git
   cd api-doacao-livros
   ```

2. Instale as dependências:

   ```
   pip install -r ./requirements.txt
   ```

3. Execute a aplicação:

   ```
   python run.py
   ```

4. (Opcional) Para popular o banco com dados de exemplo:
   ```
   python ./scripts/populate_db.py
   ```

A aplicação estará disponível em `http://localhost:5000/`.

## 📚 Endpoints da API

### 1. Página Inicial

- **URL**: `/`
- **Método**: GET
- **Descrição**: Retorna uma mensagem de boas-vindas e informações sobre as rotas disponíveis.

### 2. Listar Todos os Livros

- **URL**: `/livros`
- **Método**: GET
- **Descrição**: Retorna uma lista com todos os livros cadastrados no sistema.
- **Resposta**:
  ```json
  [
    {
      "id": 1,
      "titulo": "Dom Quixote",
      "categoria": "Romance",
      "autor": "Miguel de Cervantes",
      "imagem_url": "https://example.com/dom-quixote.jpg"
    },
    {
      "id": 2,
      "titulo": "1984",
      "categoria": "Ficção Científica",
      "autor": "George Orwell",
      "imagem_url": "https://example.com/1984.jpg"
    }
  ]
  ```

### 3. Cadastrar Novo Livro

- **URL**: `/doar`
- **Método**: POST
- **Descrição**: Cadastra um novo livro no banco de dados.
- **Corpo da Requisição**:
  ```json
  {
    "titulo": "O Senhor dos Anéis",
    "categoria": "Fantasia",
    "autor": "J.R.R. Tolkien",
    "imagem_url": "https://example.com/senhor-dos-aneis.jpg"
  }
  ```
- **Resposta (201 Created)**:
  ```json
  {
    "mensagem": "Livro cadastrado com sucesso",
    "livro": {
      "id": 3,
      "titulo": "O Senhor dos Anéis",
      "categoria": "Fantasia",
      "autor": "J.R.R. Tolkien",
      "imagem_url": "https://example.com/senhor-dos-aneis.jpg"
    }
  }
  ```

## 📂 Estrutura do Banco de Dados

### Tabela: LIVROS

- **id**: INTEGER PRIMARY KEY AUTOINCREMENT
- **titulo**: TEXT NOT NULL
- **categoria**: TEXT NOT NULL
- **autor**: TEXT NOT NULL
- **imagem_url**: TEXT NOT NULL

## 🛠️ Desenvolvido com

- [Visual Studio Code](https://code.visualstudio.com/) - Editor de código
- [Postman](https://www.postman.com/) - Plataforma de API para testar a aplicação (recomendado)
