from sqlalchemy.orm import Session
from modules.fornecedor.schemas import FornecedorCreate, Fornecedor
from core.db import SessionLocal
from sqlalchemy import text

class FornecedorRepository:
    def get_all(self):
        with SessionLocal() as session:
            query = text("SELECT id, nome, cnpj, status, empresa_id FROM fornecedor")
            result = session.execute(query).fetchall()
            return [{"id": row[0], "nome": row[1], "cnpj": row[2], "status": row[3], "empresa_id": row[4]} for row in result]

    def save(self, fornecedor: FornecedorCreate):
        with SessionLocal() as session:
            query = text("INSERT INTO fornecedor (nome, cnpj, status, empresa_id) VALUES (:nome, :cnpj, :status, :empresa_id) RETURNING id")
            result = session.execute(query, {"nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}).fetchone()
            session.commit()
            return {"id": result[0], "nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}

    def get_id(self, id: int):
        with SessionLocal() as session:
            query = text("SELECT id, nome, cnpj, status, empresa_id FROM fornecedor WHERE id = :id")
            result = session.execute(query, {"id": id}).fetchone()
            if result:
                return {"id": result[0], "nome": result[1], "cnpj": result[2], "status": result[3], "empresa_id": result[4]}
            return None

    def update(self, id: int, fornecedor: FornecedorCreate):
        with SessionLocal() as session:
            query = text("UPDATE fornecedor SET nome = :nome, cnpj = :cnpj, status = :status, empresa_id = :empresa_id WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id, "nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}).fetchone()
            session.commit()
            if result:
                return {"id": result[0], "nome": fornecedor.nome, "cnpj": fornecedor.cnpj, "status": fornecedor.status, "empresa_id": fornecedor.empresa_id}
            return None

    def delete(self, id: int):
        with SessionLocal() as session:
            query = text("DELETE FROM fornecedor WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id}).fetchone()
            session.commit()
            if result:
                return {"message": f"Fornecedor com id {id} deletado com sucesso."}
            return {"message": f"Fornecedor com id {id} não encontrado."}



