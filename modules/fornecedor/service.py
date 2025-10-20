from modules.fornecedor.repository import FornecedorRepository
from modules.fornecedor.schemas import FornecedorCreate

class FornecedorService:
    def __init__(self):
        self.repo = FornecedorRepository()

    def listar_fornecedores(self):
        return self.repo.get_all()

    def buscar_fornecedor_por_id(self, id: int):
        return self.repo.get_by_id(id)

    def criar_fornecedor(self, fornecedor: FornecedorCreate):
        return self.repo.create(fornecedor)
