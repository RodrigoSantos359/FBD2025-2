from sqlalchemy.orm import Session
from modules.produto.schemas import ProdutoCreate, Produto
from core.db import SessionLocal
from sqlalchemy import text

class ProdutoRepository:
    def get_all(self):
        with SessionLocal() as session:
            query = text("SELECT id, nome, descricao, preco, tipo_id, empresa_id, fornecedor_id FROM produto")
            result = session.execute(query).fetchall()
            return [
                {
                    "id": row[0],
                    "nome": row[1],
                    "descricao": row[2],
                    "preco": row[3],
                    "tipo_id": row[4],
                    "empresa_id": row[5],
                    "fornecedor_id": row[6],
                }
                for row in result
                if row[1] is not None and row[3] is not None and row[4] is not None and row[5] is not None and row[6] is not None
            ]

    def save(self, produto: ProdutoCreate):
        with SessionLocal() as session:
            query = text("INSERT INTO produto (nome, descricao, preco, tipo_id, empresa_id, fornecedor_id) VALUES (:nome, :descricao, :preco, :tipo_id, :empresa_id, :fornecedor_id) RETURNING id")
            result = session.execute(query, {"nome": produto.nome, "descricao": produto.descricao, "preco": produto.preco, "tipo_id": produto.tipo_id, "empresa_id": produto.empresa_id, "fornecedor_id": produto.fornecedor_id}).fetchone()
            session.commit()
            return {"id": result[0], "nome": produto.nome, "descricao": produto.descricao, "preco": produto.preco, "tipo_id": produto.tipo_id, "empresa_id": produto.empresa_id, "fornecedor_id": produto.fornecedor_id}

    def get_id(self, id: int):
        with SessionLocal() as session:
            query = text("SELECT id, nome, descricao, preco, tipo_id, empresa_id, fornecedor_id FROM produto WHERE id = :id")
            result = session.execute(query, {"id": id}).fetchone()
            if result:
                return {"id": result[0], "nome": result[1], "descricao": result[2], "preco": result[3], "tipo_id": result[4], "empresa_id": result[5], "fornecedor_id": result[6]}
            return None

    def update(self, id: int, produto: ProdutoCreate):
        with SessionLocal() as session:
            query = text("UPDATE produto SET nome = :nome, descricao = :descricao, preco = :preco, tipo_id = :tipo_id, empresa_id = :empresa_id, fornecedor_id = :fornecedor_id WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id, "nome": produto.nome, "descricao": produto.descricao, "preco": produto.preco, "tipo_id": produto.tipo_id, "empresa_id": produto.empresa_id, "fornecedor_id": produto.fornecedor_id}).fetchone()
            session.commit()
            if result:
                return {"id": result[0], "nome": produto.nome, "descricao": produto.descricao, "preco": produto.preco, "tipo_id": produto.tipo_id, "empresa_id": produto.empresa_id, "fornecedor_id": produto.fornecedor_id}
            return None

    def delete(self, id: int):
        with SessionLocal() as session:
            query = text("DELETE FROM produto WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id}).fetchone()
            session.commit()
            if result:
                return {"message": f"Produto com id {id} deletado com sucesso."}
            return {"message": f"Produto com id {id} não encontrado."}