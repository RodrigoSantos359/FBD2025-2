from sqlalchemy import Column, Integer, String
from core.db import Base

class Fornecedor(Base):
    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)