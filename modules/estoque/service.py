from modules.estoque.models import Estoque
from modules.estoque.schemas import EstoqueCreate
from datetime import datetime, timezone
from modules.produto.models import Produto

class EstoqueService:
    def __init__(self, db):
        self.db = db

    # Listar todos os estoques
    def listar_estoques(self):
        return self.db.query(Estoque).all()

    # Listar estoque por ID
    def listar_estoque_por_id(self, estoque_id: int):
        return self.db.query(Estoque).filter(Estoque.id == estoque_id).first()

    # Criar estoque
    def criar_estoque(self, estoque: EstoqueCreate):
        produto = self.db.query(Produto).filter(Produto.id == estoque.produto_id).first()
        if not produto:
            raise ValueError("Produto não encontrado")

        # Se por algum motivo ainda for string, converta para datetime
        data = estoque.data_atualizacao
        if isinstance(data, str):
            data = datetime.fromisoformat(data.replace("Z", "+00:00"))

        novo_estoque = Estoque(
            produto_id=estoque.produto_id,
            quantidade=estoque.quantidade,
            data_atualizacao=data or datetime.now(timezone.utc)
        )
        self.db.add(novo_estoque)
        self.db.commit()
        self.db.refresh(novo_estoque)

        return {
            "id": novo_estoque.id,
            "produto_id": novo_estoque.produto_id,
            "quantidade": novo_estoque.quantidade,
            "data_atualizacao": novo_estoque.data_atualizacao
        }
    # Atualizar estoque
    def atualizar_estoque(self, estoque_id: int, estoque_data: EstoqueCreate):
        estoque = self.db.query(Estoque).filter(Estoque.id == estoque_id).first()
        if not estoque:
            return None # Retorna None para o router saber que não encontrou

        # O router já garante que estoque_data é válido.
        # Atualiza apenas a quantidade, pois o produto_id não deve mudar
        estoque.quantidade = estoque_data.quantidade
        estoque.data_atualizacao = datetime.now(timezone.utc)
        self.db.commit()
        self.db.refresh(estoque)
        return estoque

    # Deletar estoque
    def deletar_estoque(self, estoque_id: int):
        estoque = self.db.query(Estoque).filter(Estoque.id == estoque_id).first()
        if not estoque:
            raise ValueError("Estoque não encontrado")
        self.db.delete(estoque)
        self.db.commit()
        return {"mensagem": "Estoque deletado com sucesso"}
