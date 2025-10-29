from modules.tipo.schemas import TipoCreate
from core.db import DataBase

class TipoRepository:
    QUERY_LISTAR = "SELECT id, nome, cod_tipo, empresa_id FROM tipo"
    QUERY_BUSCAR_ID = "SELECT id, nome, cod_tipo, empresa_id FROM tipo WHERE id = %s"
    QUERY_CRIAR = "INSERT INTO tipo (nome, cod_tipo, empresa_id) VALUES (%s, %s, %s) RETURNING id, nome, cod_tipo, empresa_id"
    QUERY_ATUALIZAR = "UPDATE tipo SET nome = %s, cod_tipo = %s, empresa_id = %s WHERE id = %s RETURNING id, nome, cod_tipo, empresa_id"
    QUERY_DELETAR = "DELETE FROM tipo WHERE id = %s"
    
    def _row_to_tipo(self, row):
        """Converte o resultado da tupla do banco de dados em um dicionário."""
        if not row:
            return None
        return {
            "id": row[0],
            "nome": row[1],
            "cod_tipo": row[2],
            "empresa_id": row[3]
        }

    def listar(self):
        db = DataBase()
        rows = db.execute(self.QUERY_LISTAR)
        return [self._row_to_tipo(row) for row in rows]

    def buscar_por_id(self, tipo_id: int):
        db = DataBase()
        row = db.execute(self.QUERY_BUSCAR_ID % tipo_id, many=False)
        return self._row_to_tipo(row)

    def criar(self, tipo: TipoCreate):
        db = DataBase()
        
        query = self.QUERY_CRIAR % (
            f"'{tipo.nome}'", 
            f"'{tipo.cod_tipo}'", 
            tipo.empresa_id
        )
        row = db.commit(query)
        
        return self._row_to_tipo(row)

    def atualizar(self, tipo_id: int, tipo_data: TipoCreate):
        db = DataBase()
        
        query = self.QUERY_ATUALIZAR % (
            f"'{tipo_data.nome}'", 
            f"'{tipo_data.cod_tipo}'", 
            tipo_data.empresa_id,
            tipo_id
        )
        row = db.commit(query)
        
        return self._row_to_tipo(row)

    def deletar(self, tipo_id: int):
        db = DataBase()
        db.commit(self.QUERY_DELETAR % tipo_id)
        return {"mensagem": "Tipo deletado com sucesso"}


