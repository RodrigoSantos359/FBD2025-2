from sqlalchemy.orm import Session
from modules.tipo.schemas import TipoCreate
from modules.tipo.models import Tipo
from core.db import SessionLocal
from sqlalchemy import text

class TipoRepository:
    def get_all(self):
        with SessionLocal() as session:
            query = text("SELECT id, nome, cod_tipo, empresa_id FROM tipo")
            result = session.execute(query).fetchall()
            return [{"id": row[0], "nome": row[1], "cod_tipo": row[2], "empresa_id": row[3]} for row in result]

    def save(self, tipo: TipoCreate):
        with SessionLocal() as session:
            query = text("INSERT INTO tipo (nome, cod_tipo, empresa_id) VALUES (:nome, :cod_tipo, :empresa_id) RETURNING id")
            result = session.execute(query, {"nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}).fetchone()
            session.commit()
            return {"id": result[0], "nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}

    def get_id(self, id: int):
        with SessionLocal() as session:
            query = text("SELECT id, nome, cod_tipo, empresa_id FROM tipo WHERE id = :id")
            result = session.execute(query, {"id": id}).fetchone()
            if result:
                return {"id": result[0], "nome": result[1], "cod_tipo": result[2], "empresa_id": result[3]}
            return None

    def update(self, id: int, tipo: TipoCreate):
        with SessionLocal() as session:
            query = text("UPDATE tipo SET nome = :nome, cod_tipo = :cod_tipo, empresa_id = :empresa_id WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id, "nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}).fetchone()
            session.commit()
            if result:
                return {"id": result[0], "nome": tipo.nome, "cod_tipo": tipo.cod_tipo, "empresa_id": tipo.empresa_id}
            return None

    def delete(self, id: int):
        with SessionLocal() as session:
            query = text("DELETE FROM tipo WHERE id = :id RETURNING id")
            result = session.execute(query, {"id": id}).fetchone()
            session.commit()
            if result:
                return {"message": f"Tipo com id {id} deletado com sucesso."}
            return {"message": f"Tipo com id {id} não encontrado."}