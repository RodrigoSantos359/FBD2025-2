from modules.estoque.repository import EstoqueRepository
from modules.estoque.schemas import EstoqueCreate

class EstoqueService:
    
    # Listar todos os estoques
    def listar_estoques(self):
        return EstoqueRepository().listar()

    # Listar estoque por ID
    def listar_estoque_por_id(self, estoque_id: int):
        return EstoqueRepository().buscar_por_id(estoque_id)

    # Criar estoque
    def criar_estoque(self, estoque: EstoqueCreate):
        # A verificação de produto_id foi movida para o Repository
        return EstoqueRepository().criar(estoque)

    # Atualizar estoque
    def atualizar_estoque(self, estoque_id: int, estoque_data: EstoqueCreate):
        # A verificação de existência foi movida para o Repository
        return EstoqueRepository().atualizar(estoque_id, estoque_data)

    # Deletar estoque
    def deletar_estoque(self, estoque_id: int):
        # O Repository não faz a verificação de existência antes de deletar, então fazemos aqui
        estoque = EstoqueRepository().buscar_por_id(estoque_id)
        if not estoque:
            raise ValueError("Estoque não encontrado")
            
        EstoqueRepository().deletar(estoque_id)
        return {"mensagem": "Estoque deletado com sucesso"}

