from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.db import Base
from datetime import datetime

class Estoque(Base):
    __tablename__ = "estoque"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, nullable=False)

    produto = relationship("Produto", back_populates="estoques")