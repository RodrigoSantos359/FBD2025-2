from core.db import get_db
from modules.company.schemas import CompanyCreate
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        query = text("SELECT id, nome, cnpj, status FROM empresa")
        results = self.db.execute(query).fetchall()
        return [{"id": row[0], "nome": row[1], "cnpj": row[2], "status": row[3]} for row in results]

    def save(self, company: CompanyCreate):
        query = text("INSERT INTO empresa (nome, cnpj, status) VALUES (:nome, :cnpj, :status) RETURNING id")
        result = self.db.execute(query, {"nome": company.nome, "cnpj": company.cnpj, "status": company.status}).fetchone()
        self.db.commit()
        return {"id": result[0], "nome": company.nome, "cnpj": company.cnpj, "status": company.status}

    def get_id(self, id: int):
        query = text("SELECT id, nome, cnpj, status FROM empresa WHERE id = :id")
        result = self.db.execute(query, {"id": id}).fetchone()
        if result:
            return {"id": result[0], "nome": result[1], "cnpj": result[2], "status": result[3]}
        return {}

    def update(self, id: int, company: CompanyCreate):
        query = text("UPDATE empresa SET nome = :nome, cnpj = :cnpj, status = :status WHERE id = :id RETURNING id, nome, cnpj, status")
        result = self.db.execute(query, {"id": id, "nome": company.nome, "cnpj": company.cnpj, "status": company.status}).fetchone()
        self.db.commit()
        if result:
            return {"id": result[0], "nome": result[1], "cnpj": result[2], "status": result[3]}
        return None

    def delete(self, id: int):
        query = text("DELETE FROM empresa WHERE id = :id RETURNING id")
        result = self.db.execute(query, {"id": id}).fetchone()
        self.db.commit()
        if result:
            return {"message": f"Empresa com id {id} deletada com sucesso."}
        return {"message": f"Empresa com id {id} não encontrada."}