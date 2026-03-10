# API (FastAPI)

API do projeto Epidemia desenvolvida em Python com FastAPI.

## Requisitos

- Python 3.13
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes)

## Instalação

### 1. Instalar o uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Instalar o Python 3.13

```bash
uv python install 3.13
```

### 3. Instalar dependências

```bash
make install
```

### 4. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

## Executando a API

```bash
make dev      # desenvolvimento (hot reload)
make test     # rodar testes
make lint     # verificar código
make format   # formatar código
```

A API estará disponível em `http://localhost:8080`.

## Documentação

- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Health check |

## Estrutura

```
api/
├── src/
│   ├── __init__.py
│   ├── main.py           # Aplicação FastAPI
│   ├── config.py         # Configurações
│   └── routers/
│       ├── __init__.py
│       └── health.py     # Rotas de health check
├── tests/
│   └── __init__.py
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore
├── Makefile
├── pyproject.toml
└── README.md
```

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| PORT | Porta da API | 8080 |
