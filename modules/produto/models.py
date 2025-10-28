from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    tipo_id = Column(Integer, ForeignKey("tipo.id"), nullable=False)
    fornecedor_id = Column(Integer, ForeignKey("fornecedor.id"), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

    tipo = relationship("Tipo", back_populates="produtos")
    fornecedor = relationship("Fornecedor", back_populates="produtos")
    empresa = relationship("Empresa", back_populates="produtos")
    estoques = relationship("Estoque", back_populates="produto")