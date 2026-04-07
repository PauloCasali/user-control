# User Control API

Sistema simples de controle de usuários com autenticação (register, login, CRUD de usuários).

Projeto desenvolvido com *Docker + Docker Compose* para facilitar o desenvolvimento e execução local.

## Tecnologias Utilizadas

- *Backend*: FastAPI (Python3)
- *Banco de dados*: PostgreSQL 
- *Containerização*: Docker + Docker Compose
- *ORM*: Sqlalchemy

## Funcionalidades

- Cadastro de usuário (Post/users)
- Listagem de usuários (Get/users)

## Pré-requisitos

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/) (vem junto com o Docker Desktop na maioria dos casos)
- [Python](https://www.python.org/) instalado
- [PostgreSql](https://www.postgresql.org/) instalado

## Como rodar o projeto

*Clone o repositório*: git clone https://github.com/PauloCasali/user-control.git

*Copie o arquivo de ambiente:* cp .env.example .env

*Suba os containers com Docker:* docker-compose up -d --build

*Acesse a aplicação:* Documentação (Swagger): http://localhost:8000/docs

No docs abrirá 1 janela com swagger para testar os endpoint disponíveis