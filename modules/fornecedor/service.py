from modules.fornecedor import schemas
from modules.fornecedor.repository import FornecedorRepository

class FornecedorService:
    def get_fornecedores(self):
        repository = FornecedorRepository()
        return repository.listar()

    def create_fornecedor(self, fornecedor: schemas.FornecedorCreate):
        repository = FornecedorRepository()
        return repository.criar(fornecedor)

    def get_fornecedor_id(self, id: int):
        repository = FornecedorRepository()
        return repository.buscar_por_id(id)

    def update_fornecedor(self, id: int, fornecedor: schemas.FornecedorCreate):
        repository = FornecedorRepository()
        return repository.atualizar(id, fornecedor)

    def delete_fornecedor(self, id: int):
        repository = FornecedorRepository()
        return repository.deletar(id)