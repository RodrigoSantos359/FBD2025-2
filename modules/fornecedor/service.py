from typing import Optional
from modules.fornecedor import schemas
from modules.fornecedor.repository import FornecedorRepository

class FornecedorService:
    def get_fornecedores(self):
        repository = FornecedorRepository()
        return repository.get_all()

    def create_fornecedor(self, fornecedor: schemas.FornecedorCreate) -> schemas.Fornecedor:
        repository = FornecedorRepository()
        return repository.save(fornecedor)

    def get_fornecedor_id(self, id: int):
        repository = FornecedorRepository()
        return repository.get_id(id)

    def update_fornecedor(self, id: int, fornecedor: schemas.FornecedorCreate) -> Optional[schemas.Fornecedor]:
        repository = FornecedorRepository()
        return repository.update(id, fornecedor)

    def delete_fornecedor(self, id: int):
        repository = FornecedorRepository()
        return repository.delete(id)