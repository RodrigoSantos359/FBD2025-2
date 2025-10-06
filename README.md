# FastAPI Project - Sistema de Estoque

API REST desenvolvida com FastAPI para gerenciamento de empresas (sistema de estoque).

## Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI** - Framework web moderno e de alta performance
- **PostgreSQL** - Banco de dados relacional
- **psycopg2** - Driver PostgreSQL para Python
- **Uvicorn** - Servidor ASGI para aplicações Python
- **Pydantic** - Validação de dados

## Estrutura do Projeto

```
fastApiProject/
├── api/
│   └── routes/
│       └── company_routes.py    # Rotas da API de empresas
├── core/
│   ├── db.py                    # Configuração do banco de dados
│   └── settings.py              # Configurações do projeto
├── modules/
│   └── company/
│       ├── repository.py        # Camada de acesso a dados
│       ├── schemas.py           # Schemas Pydantic
│       └── service.py           # Lógica de negócio
├── main.py                      # Arquivo principal da aplicação
└── venv/                        # Ambiente virtual Python
```

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e rodando
- pip (gerenciador de pacotes Python)

## Configuração do Banco de Dados

1. Certifique-se de que o PostgreSQL está instalado e rodando
2. Crie um banco de dados chamado `sistema_estoque_aula`:

```sql
CREATE DATABASE sistema_estoque_aula;
```

3. As configurações padrão do banco estão definidas em `core/settings.py`:
   - **Host:** localhost
   - **Porta:** 5432
   - **Usuário:** postgres
   - **Senha:** postgres
   - **Database:** sistema_estoque_aula

4. Ajuste essas configurações conforme necessário no arquivo `core/settings.py`

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositório>
cd fastApiProject
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/Mac
# ou
venv\Scripts\activate  # No Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não existir, instale as dependências manualmente:
```bash
pip install fastapi==0.118.0 uvicorn==0.37.0 psycopg2==2.9.10 pydantic==2.11.9 python-dotenv==1.1.1
```

## Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado
2. Execute o servidor de desenvolvimento:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em: `http://localhost:8000`

### Opções adicionais de execução:

```bash
# Especificar porta diferente
uvicorn main:app --reload --port 8080

# Permitir acesso externo
uvicorn main:app --reload --host 0.0.0.0

# Com log detalhado
uvicorn main:app --reload --log-level debug
```

## Endpoints da API

### Empresas (Company)

- **GET `/`** - Endpoint raiz
  - Retorna: `{"Hello": "World"}`

- **GET `/company/`** - Lista todas as empresas
  - Retorna: Array de objetos Company

- **GET `/company/{id}/`** - Busca empresa por ID
  - Parâmetro: `id` (inteiro)
  - Retorna: Objeto Company ou null

- **POST `/company/`** - Cria nova empresa
  - Body: Objeto CompanyCreate (JSON)
  - Retorna: Objeto Company criado

## Documentação Interativa

O FastAPI gera automaticamente documentação interativa da API:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## Testando a API

### Usando curl:

```bash
# Listar empresas
curl http://localhost:8000/company/

# Buscar empresa por ID
curl http://localhost:8000/company/1/

# Criar nova empresa
curl -X POST http://localhost:8000/company/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Minha Empresa", "cnpj": "12345678000190"}'
```

### Usando o arquivo test_main.http:

O projeto inclui o arquivo `test_main.http` que pode ser usado com extensões HTTP Client do PyCharm ou VS Code.

## Desenvolvimento

### Estrutura de Camadas

O projeto segue uma arquitetura em camadas:

1. **Routes** (`api/routes/`) - Define os endpoints da API
2. **Service** (`modules/company/service.py`) - Implementa a lógica de negócio
3. **Repository** (`modules/company/repository.py`) - Gerencia acesso aos dados
4. **Schemas** (`modules/company/schemas.py`) - Define modelos de dados com Pydantic

### Boas Práticas

- O ambiente virtual (`venv/`) deve ser sempre ativado antes de trabalhar no projeto
- Não commitar o diretório `venv/` no Git (já está no `.gitignore`)
- Atualizar `requirements.txt` ao adicionar novas dependências:
  ```bash
  pip freeze > requirements.txt
  ```

## Troubleshooting

### Erro de conexão com PostgreSQL

Se receber erro de conexão com o banco:
1. Verifique se o PostgreSQL está rodando: `sudo service postgresql status`
2. Confirme as credenciais em `core/settings.py`
3. Verifique se o banco `sistema_estoque_aula` foi criado

### Erro ao importar módulos

Se houver erros de importação:
1. Certifique-se de que o ambiente virtual está ativado
2. Reinstale as dependências: `pip install -r requirements.txt`

### Porta já em uso

Se a porta 8000 já estiver em uso:
```bash
# Use outra porta
uvicorn main:app --reload --port 8080
```

## Licença

[Adicione aqui a licença do projeto]

## Contato

[Adicione aqui informações de contato ou links relevantes]
