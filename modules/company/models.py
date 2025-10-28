from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from core.db import Base
from modules.fornecedor.models import Fornecedor

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    status = Column(
        Enum("ATIVO", "INATIVO", "SUSPENSO", name="empresa_status"),
        default="ATIVO",
        nullable=False
    )

    tipos = relationship("Tipo", back_populates="empresa")
    fornecedores = relationship(Fornecedor, back_populates="empresa")
    produtos = relationship("Produto", back_populates="empresa")