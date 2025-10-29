from modules.produto import schemas
from modules.produto.repository import ProdutoRepository

class ProdutoService:
    def get_produtos(self):
        repository = ProdutoRepository()
        return repository.listar()

    def create_produto(self, produto: schemas.ProdutoCreate):
        repository = ProdutoRepository()
        return repository.criar(produto)

    def get_produto_id(self, id: int):
        repository = ProdutoRepository()
        return repository.buscar_por_id(id)

    def update_produto(self, id: int, produto: schemas.ProdutoCreate):
        repository = ProdutoRepository()
        return repository.atualizar(id, produto)

    def delete_produto(self, id: int):
        repository = ProdutoRepository()
        return repository.deletar(id)