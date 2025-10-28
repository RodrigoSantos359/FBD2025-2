from typing import Optional
from modules.produto import schemas
from modules.produto.repository import ProdutoRepository

class ProdutoService:
    def get_produtos(self):
        repository = ProdutoRepository()
        return repository.get_all()

    def create_produto(self, produto: schemas.ProdutoCreate) -> schemas.Produto:
        repository = ProdutoRepository()
        return repository.save(produto)

    def get_produto_id(self, id: int):
        repository = ProdutoRepository()
        return repository.get_id(id)

    def update_produto(self, id: int, produto: schemas.ProdutoCreate) -> Optional[schemas.Produto]:
        repository = ProdutoRepository()
        return repository.update(id, produto)

    def delete_produto(self, id: int):
        repository = ProdutoRepository()
        return repository.delete(id)