from core.db import SessionLocal
from modules.fornecedor.schemas import FornecedorCreate
from modules.fornecedor.models import Fornecedor

class FornecedorRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Fornecedor).all()

    def get_by_id(self, id: int):
        return self.db.query(Fornecedor).filter(Fornecedor.id == id).first()

    def create(self, fornecedor: FornecedorCreate):
        db_fornecedor = Fornecedor(**fornecedor.dict())
        self.db.add(db_fornecedor)
        self.db.commit()
        self.db.refresh(db_fornecedor)
        return db_fornecedor
