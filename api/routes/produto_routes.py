from typing import Optional

from fastapi import APIRouter, HTTPException

from modules.produto import schemas
from modules.produto.schemas import ProdutoCreate
from modules.produto.service import ProdutoService

router = APIRouter(prefix="/produto", tags=["Produto"])


@router.get("/", response_model=list[schemas.Produto])
def list_produtos():
    service = ProdutoService()
    return service.get_produtos()


@router.get("/{id}/", response_model=Optional[schemas.Produto])
def get_produto_by_id(id: int):
    service = ProdutoService()
    produto = service.get_produto_id(id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.post("/", response_model=schemas.Produto)
def create_produto(produto: ProdutoCreate):
    service = ProdutoService()
    return service.create_produto(produto)


@router.put("/{id}/", response_model=schemas.Produto)
def update_produto(id: int, produto: ProdutoCreate):
    service = ProdutoService()
    updated_produto = service.update_produto(id, produto)
    if not updated_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_produto


@router.delete("/{id}/")
def delete_produto(id: int):
    service = ProdutoService()
    result = service.delete_produto(id)
    if "não encontrado" in result.get("message", ""):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result