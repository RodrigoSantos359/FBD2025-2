import sys
import os
from core.db import DataBase
import psycopg2

# Adiciona o diretório raiz do projeto ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Comandos SQL para criar as tabelas
# Mantendo a estrutura original de chaves primárias e estrangeiras
SQL_CREATE_TABLES = [
    """
    DROP TABLE IF EXISTS estoque;
    DROP TABLE IF EXISTS produto;
    DROP TABLE IF EXISTS fornecedor;
    DROP TABLE IF EXISTS tipo;
    DROP TABLE IF EXISTS empresa;
    CREATE TABLE IF NOT EXISTS empresa (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cnpj VARCHAR(18) UNIQUE NOT NULL,
        status VARCHAR(50) NOT NULL DEFAULT 'ATIVO'
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS tipo (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cod_tipo VARCHAR(50) NOT NULL,
        empresa_id INTEGER REFERENCES empresa(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS fornecedor (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cnpj VARCHAR(18) UNIQUE NOT NULL,
        status VARCHAR(50) NOT NULL DEFAULT 'ATIVO',
        empresa_id INTEGER REFERENCES empresa(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS produto (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        descricao TEXT,
        preco NUMERIC(10, 2) NOT NULL,
        tipo_id INTEGER NOT NULL REFERENCES tipo(id),
        fornecedor_id INTEGER NOT NULL REFERENCES fornecedor(id),
        empresa_id INTEGER NOT NULL REFERENCES empresa(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS estoque (
        id SERIAL PRIMARY KEY,
        produto_id INTEGER NOT NULL REFERENCES produto(id),
        quantidade INTEGER NOT NULL,
        data_atualizacao TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    );
    """
]

def create_tables():
    print("Conectando ao banco de dados...")
    try:
        # Cria uma instância de DataBase
        db = DataBase()
        
        # O DataBase.commit/execute fecha a conexão. 
        # Vamos usar uma conexão temporária para cada comando SQL.
        for sql_command in SQL_CREATE_TABLES:
            # Reabre a conexão para cada comando
            temp_db = DataBase()
            print(f"Executando: {sql_command.splitlines()[1].strip()}...")
            # O método commit/execute é usado para rodar comandos DDL/DML
            # O commit é mais apropriado para DDL (CREATE TABLE)
            temp_db.commit(sql_command)
            
        print("Tabelas criadas com sucesso.")

    except psycopg2.OperationalError as e:
        print(f"Erro de Conexão/Operação: {e}")
        print("Certifique-se de que o servidor PostgreSQL está rodando e as configurações em settings.py estão corretas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    create_tables()


