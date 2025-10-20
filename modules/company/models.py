from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base

class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    # Relacionamento com a tabela Tipo
    tipos = relationship("Tipo", back_populates="empresa")