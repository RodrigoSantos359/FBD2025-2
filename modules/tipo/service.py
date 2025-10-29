from modules.tipo import schemas
from modules.tipo.repository import TipoRepository

class TipoService:
    def get_tipos(self):
        repository = TipoRepository()
        return repository.listar()

    def create_tipo(self, tipo: schemas.TipoCreate):
        repository = TipoRepository()
        return repository.criar(tipo)

    def get_tipo_id(self, id: int):
        repository = TipoRepository()
        return repository.buscar_por_id(id)

    def update_tipo(self, id: int, tipo: schemas.TipoCreate):
        repository = TipoRepository()
        return repository.atualizar(id, tipo)

    def delete_tipo(self, id: int):
        repository = TipoRepository()
        return repository.deletar(id)