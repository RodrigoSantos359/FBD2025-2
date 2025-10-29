from core.db import DataBase
from modules.produto.schemas import ProdutoCreate

class ProdutoRepository:
    QUERY_LISTAR = "SELECT id, nome, descricao, preco, tipo_id, fornecedor_id, empresa_id FROM produto"
    QUERY_BUSCAR_ID = "SELECT id, nome, descricao, preco, tipo_id, fornecedor_id, empresa_id FROM produto WHERE id = %s"
    QUERY_CRIAR = "INSERT INTO produto (nome, descricao, preco, tipo_id, fornecedor_id, empresa_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id, nome, descricao, preco, tipo_id, fornecedor_id, empresa_id"
    QUERY_ATUALIZAR = "UPDATE produto SET nome = %s, descricao = %s, preco = %s, tipo_id = %s, fornecedor_id = %s, empresa_id = %s WHERE id = %s RETURNING id, nome, descricao, preco, tipo_id, fornecedor_id, empresa_id"
    QUERY_DELETAR = "DELETE FROM produto WHERE id = %s"
    
    def _row_to_produto(self, row):
        """Converte o resultado da tupla do banco de dados em um dicionário."""
        if not row:
            return None
        return {
            "id": row[0],
            "nome": row[1],
            "descricao": row[2],
            "preco": row[3],
            "tipo_id": row[4],
            "fornecedor_id": row[5],
            "empresa_id": row[6]
        }

    def listar(self):
        db = DataBase()
        rows = db.execute(self.QUERY_LISTAR)
        return [self._row_to_produto(row) for row in rows]

    def buscar_por_id(self, produto_id: int):
        db = DataBase()
        # Nota: O seu DataBase.execute não usa placeholders, então formatamos a string
        row = db.execute(self.QUERY_BUSCAR_ID % produto_id, many=False)
        return self._row_to_produto(row)

    def criar(self, produto: ProdutoCreate):
        db = DataBase()
        
        # Formatação de string para SQL: valores numéricos diretos, strings entre aspas simples
        query = self.QUERY_CRIAR % (
            f"'{produto.nome}'", 
            f"'{produto.descricao}'", 
            produto.preco, 
            produto.tipo_id, 
            produto.fornecedor_id, 
            produto.empresa_id
        )
        row = db.commit(query)
        
        return self._row_to_produto(row)

    def atualizar(self, produto_id: int, produto_data: ProdutoCreate):
        db = DataBase()
        
        query = self.QUERY_ATUALIZAR % (
            f"'{produto_data.nome}'", 
            f"'{produto_data.descricao}'", 
            produto_data.preco, 
            produto_data.tipo_id, 
            produto_data.fornecedor_id, 
            produto_data.empresa_id,
            produto_id
        )
        row = db.commit(query)
        
        return self._row_to_produto(row)

    def deletar(self, produto_id: int):
        db = DataBase()
        db.commit(self.QUERY_DELETAR % produto_id)
        return {"mensagem": "Produto deletado com sucesso"}


