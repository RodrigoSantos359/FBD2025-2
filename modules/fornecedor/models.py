from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base

class Fornecedor(Base):
    __tablename__ = "fornecedor"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    status = Column(Enum("ATIVO", "INATIVO", "SUSPENSO", name="fornecedor_status"),
        default="ATIVO",
        nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresa.id"))

    empresa = relationship("Empresa", back_populates="fornecedores")
    produtos = relationship("Produto", back_populates="fornecedor")