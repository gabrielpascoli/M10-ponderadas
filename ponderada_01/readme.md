# API de Gerenciamento de Tarefas

Esta é uma API simples para gerenciamento de tarefas desenvolvida usando Flask.

## Funcionalidades

- Autenticação de usuário e geração de token JWT
- CRUD (Criar, Ler, Atualizar, Deletar) de tarefas
- Interface de usuário para login, registro e exibição de conteúdo secreto

## Requisitos

- Python
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/M10-ponderadas.git
cd M10-ponderadas

Instale as dependências:
bash
Copy code
pip install -r requirements.txt
Crie o Banco de Dados:
bash
Copy code
python main.py create_db
Execute a API:
bash
Copy code
python main.py
A aplicação estará disponível em http://localhost:5000.

Documentação da API
A documentação da API pode ser encontrada aqui. Esta documentação fornece informações detalhadas sobre todas as rotas disponíveis, os parâmetros necessários e exemplos de uso.

Testes de Rotas
Você pode interagir com a API usando qualquer cliente HTTP ou ferramenta de desenvolvimento de API. Aqui está um exemplo usando o Insomnia para obter todas as tarefas:

Insomnia