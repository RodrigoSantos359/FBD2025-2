from modules.fornecedor.schemas import FornecedorCreate
from core.db import DataBase

class FornecedorRepository:
    QUERY_LISTAR = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor"
    QUERY_BUSCAR_ID = "SELECT id, nome, cnpj, status, empresa_id FROM fornecedor WHERE id = %s"
    QUERY_CRIAR = "INSERT INTO fornecedor (nome, cnpj, status, empresa_id) VALUES (%s, %s, %s, %s) RETURNING id, nome, cnpj, status, empresa_id"
    QUERY_ATUALIZAR = "UPDATE fornecedor SET nome = %s, cnpj = %s, status = %s, empresa_id = %s WHERE id = %s RETURNING id, nome, cnpj, status, empresa_id"
    QUERY_DELETAR = "DELETE FROM fornecedor WHERE id = %s"
    
    def _row_to_fornecedor(self, row):
        """Converte o resultado da tupla do banco de dados em um dicionário."""
        if not row:
            return None
        return {
            "id": row[0],
            "nome": row[1],
            "cnpj": row[2],
            "status": row[3],
            "empresa_id": row[4]
        }

    def listar(self):
        db = DataBase()
        rows = db.execute(self.QUERY_LISTAR)
        return [self._row_to_fornecedor(row) for row in rows]

    def buscar_por_id(self, fornecedor_id: int):
        db = DataBase()
        row = db.execute(self.QUERY_BUSCAR_ID % fornecedor_id, many=False)
        return self._row_to_fornecedor(row)

    def criar(self, fornecedor: FornecedorCreate):
        db = DataBase()
        
        query = self.QUERY_CRIAR % (
            f"'{fornecedor.nome}'", 
            f"'{fornecedor.cnpj}'", 
            f"'{fornecedor.status.value}'", # Enum deve ser convertido para string
            fornecedor.empresa_id
        )
        row = db.commit(query)
        
        return self._row_to_fornecedor(row)

    def atualizar(self, fornecedor_id: int, fornecedor_data: FornecedorCreate):
        db = DataBase()
        
        query = self.QUERY_ATUALIZAR % (
            f"'{fornecedor_data.nome}'", 
            f"'{fornecedor_data.cnpj}'", 
            f"'{fornecedor_data.status.value}'", # Enum deve ser convertido para string
            fornecedor_data.empresa_id,
            fornecedor_id
        )
        row = db.commit(query)
        
        return self._row_to_fornecedor(row)

    def deletar(self, fornecedor_id: int):
        db = DataBase()
        db.commit(self.QUERY_DELETAR % fornecedor_id)
        return {"mensagem": "Fornecedor deletado com sucesso"}


