from modules.tipo.repository import TipoRepository
from modules.tipo.schemas import TipoCreate
from modules.tipo.schemas import TipoBase
from modules.company.models import Empresa
from fastapi import HTTPException

class TipoService:
    def __init__(self):
        self.repo = TipoRepository()

    def listar_tipos(self):
        return self.repo.get_all()

    def buscar_tipo_por_id(self, id: int):
        return self.repo.get_by_id(id)
    
    def criar_tipo_com_id(self, tipo: TipoBase):
        try:
            return self.repo.create_with_id(tipo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def criar_tipo(self, tipo: TipoCreate):
        # Validate empresa_id
        # with self.repo.db as session:
        #     empresa_exists = session.query(Empresa).filter(Empresa.id == tipo.empresa_id).first()
        #     if not empresa_exists:
        #         raise HTTPException(status_code=400, detail=f"Empresa with id {tipo.empresa_id} does not exist.")

        return self.repo.create(tipo)
