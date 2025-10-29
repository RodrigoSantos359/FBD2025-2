from datetime import datetime, timezone
from modules.estoque.schemas import EstoqueCreate
from core.db import DataBase

class EstoqueRepository:
    QUERY_LISTAR = "SELECT id, produto_id, quantidade, data_atualizacao FROM estoque"
    QUERY_BUSCAR_ID = "SELECT id, produto_id, quantidade, data_atualizacao FROM estoque WHERE id = %s"
    QUERY_CRIAR = "INSERT INTO estoque (produto_id, quantidade, data_atualizacao) VALUES (%s, %s, %s) RETURNING id, produto_id, quantidade, data_atualizacao"
    QUERY_ATUALIZAR = "UPDATE estoque SET quantidade = %s, data_atualizacao = %s WHERE id = %s RETURNING id, produto_id, quantidade, data_atualizacao"
    QUERY_DELETAR = "DELETE FROM estoque WHERE id = %s"
    
    # Query auxiliar para verificar se o produto existe
    QUERY_BUSCAR_PRODUTO = "SELECT id FROM produto WHERE id = %s"

    def _row_to_estoque(self, row):
        """Converte o resultado da tupla do banco de dados em um dicionário."""
        if not row:
            return None
        # O psycopg2 retorna datetime.datetime, que é serializável pelo FastAPI/Pydantic
        return {
            "id": row[0],
            "produto_id": row[1],
            "quantidade": row[2],
            "data_atualizacao": row[3]
        }

    def listar(self):
        db = DataBase()
        rows = db.execute(self.QUERY_LISTAR)
        return [self._row_to_estoque(row) for row in rows]

    def buscar_por_id(self, estoque_id: int):
        db = DataBase()
        row = db.execute(self.QUERY_BUSCAR_ID % estoque_id, many=False)
        return self._row_to_estoque(row)

    def criar(self, estoque: EstoqueCreate):
        db = DataBase()
        
        # 1. Verificar se o produto existe (SQL puro)
        # Nota: O seu DataBase.execute não usa placeholders, então formatamos a string
        produto_existe = db.execute(self.QUERY_BUSCAR_PRODUTO % estoque.produto_id, many=False)
        if not produto_existe:
            raise ValueError("Produto não encontrado")
            
        # 2. Preparar dados para inserção
        data_atualizacao = estoque.data_atualizacao or datetime.now(timezone.utc)
        
        # 3. Executar o INSERT
        # Formatação de string para SQL: valores numéricos diretos, datas entre aspas simples
        query = self.QUERY_CRIAR % (estoque.produto_id, estoque.quantidade, f"'{data_atualizacao}'")
        row = db.commit(query)
        
        return self._row_to_estoque(row)

    def atualizar(self, estoque_id: int, estoque_data: EstoqueCreate):
        db = DataBase()
        
        data_atualizacao = datetime.now(timezone.utc)
        
        # Formatação de string para SQL: valores numéricos diretos, datas entre aspas simples
        query = self.QUERY_ATUALIZAR % (estoque_data.quantidade, f"'{data_atualizacao}'", estoque_id)
        row = db.commit(query)
        
        return self._row_to_estoque(row)

    def deletar(self, estoque_id: int):
        db = DataBase()
        
        # Executar o DELETE
        query = self.QUERY_DELETAR % estoque_id
        db.commit(query)
        
        # Como o commit do seu DataBase não retorna o registro deletado, 
        # o service terá que lidar com a verificação de existência antes de chamar o delete.
        return {"mensagem": "Estoque deletado com sucesso"}


