from typing import Optional
from modules.tipo import schemas
from modules.tipo.repository import TipoRepository

class TipoService:
    def get_tipos(self):
        repository = TipoRepository()
        return repository.get_all()

    def create_tipo(self, tipo: schemas.TipoCreate) -> schemas.Tipo:
        repository = TipoRepository()
        return repository.save(tipo)

    def get_tipo_id(self, id: int):
        repository = TipoRepository()
        return repository.get_id(id)

    def update_tipo(self, id: int, tipo: schemas.TipoCreate) -> Optional[schemas.Tipo]:
        repository = TipoRepository()
        return repository.update(id, tipo)

    def delete_tipo(self, id: int):
        repository = TipoRepository()
        return repository.delete(id)