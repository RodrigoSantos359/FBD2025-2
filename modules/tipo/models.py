from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
from modules.company.models import Empresa

class Tipo(Base):
    __tablename__ = "tipo"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cod_tipo = Column(String, unique=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresa.id"))

    # Relacionamento com a tabela empresa (se necessário)
    empresa = relationship("Empresa", back_populates="tipos")

    # 

    
