from http.client import HTTPException
from core.db import SessionLocal
from modules.company.models import Empresa
from modules.tipo.schemas import TipoCreate
from modules.tipo.models import Tipo  # se tiver model SQLAlchemy
from modules.tipo.schemas import TipoBase
from sqlalchemy.exc import IntegrityError

class TipoRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Tipo).all()

    def get_by_id(self, id: int):
        return self.db.query(Tipo).filter(Tipo.id == id).first()

    def create(self, tipo: TipoCreate):
        db_tipo = Tipo(**tipo.dict())
        self.db.add(db_tipo)
        self.db.commit()
        self.db.refresh(db_tipo)
        return db_tipo
    
    def close(self):
        self.db.close() 

    def create_with_id(self, tipo: TipoBase):
        """
        Create a new Tipo entry with the provided ID.
        """
        try:
            # Check if a record with the same cod_tipo and empresa_id already exists
            existing_tipo = self.db.query(Tipo).filter_by(
                cod_tipo=tipo.cod_tipo, empresa_id=tipo.empresa_id
            ).first()

            if existing_tipo:
                raise ValueError(
                    f"A Tipo with cod_tipo '{tipo.cod_tipo}' and empresa_id '{tipo.empresa_id}' already exists."
                )

            # Add the new Tipo to the session
            self.db.add(tipo)
            self.db.commit()
            return tipo

        except IntegrityError as e:
            self.db.rollback()
            raise ValueError("Failed to create Tipo due to a database integrity error.") from e

        except ValueError as e:
            self.db.rollback()
            raise e
