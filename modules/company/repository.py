from sqlalchemy.orm import Session
from modules.company.schemas import CompanyCreate
from core.db import SessionLocal
from sqlalchemy import text

class CompanyRepository:
    def get_all(self):
        with SessionLocal() as session:
            query = text("SELECT id, nome FROM company")
            result = session.execute(query).fetchall()
            return [{"id": row[0], "name": row[1]} for row in result]

    def save(self, company: CompanyCreate):
        with SessionLocal() as session:
            query = text("INSERT INTO company (nome, cnpj) VALUES (:name, :cnpj) RETURNING id")
            result = session.execute(query, {"name": company.name, "cnpj": company.cnpj}).fetchone()
            session.commit()
            return {"id": result[0], "name": company.name, "cnpj": company.cnpj}

    def get_id(self, id: int):
        with SessionLocal() as session:
            query = text("SELECT id, nome, cnpj FROM company WHERE id = :id")
            result = session.execute(query, {"id": id}).fetchone()
            if result:
                return {"id": result[0], "name": result[1], "cnpj": result[2]}
            return {}