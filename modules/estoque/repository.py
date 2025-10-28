from typing import List, Optional
from sqlalchemy.orm import Session
from modules.estoque.models import Estoque

class EstoqueRepository:
    def __init__(self, session: Session):
        self.session = session

    def criar_estoque(self, estoque: Estoque) -> Estoque:
        try:
            self.session.add(estoque)
            self.session.commit()
            self.session.refresh(estoque)
            return estoque
        except Exception as e:
            self.session.rollback()
            raise e

    def buscar_estoque_por_id(self, estoque_id: int) -> Optional[Estoque]:
        return self.session.query(Estoque).filter(Estoque.id == estoque_id).first()

    def listar_estoques(self) -> List[Estoque]:
        return self.session.query(Estoque).all()

    def atualizar_estoque(self, estoque: Estoque) -> Estoque:
        try:
            self.session.merge(estoque)
            self.session.commit()
            self.session.refresh(estoque)
            return estoque
        except Exception as e:
            self.session.rollback()
            raise e

    def deletar_estoque(self, estoque_id: int) -> bool:
        try:
            estoque = self.buscar_estoque_por_id(estoque_id)
            if estoque:
                self.session.delete(estoque)
                self.session.commit()
                return True
            return False
        except Exception as e:
            self.session.rollback()
            raise e