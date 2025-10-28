from typing import Optional

from fastapi import APIRouter, HTTPException

from modules.fornecedor import schemas
from modules.fornecedor.schemas import FornecedorCreate
from modules.fornecedor.service import FornecedorService

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])


@router.get("/", response_model=list[schemas.Fornecedor])
def list_fornecedores():
    service = FornecedorService()
    return service.get_fornecedores()


@router.get("/{id}/", response_model=Optional[schemas.Fornecedor])
def get_fornecedor_by_id(id: int):
    service = FornecedorService()
    fornecedor = service.get_fornecedor_id(id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor


@router.post("/", response_model=schemas.Fornecedor)
def create_fornecedor(fornecedor: FornecedorCreate):
    service = FornecedorService()
    return service.create_fornecedor(fornecedor)


@router.put("/{id}/", response_model=schemas.Fornecedor)
def update_fornecedor(id: int, fornecedor: FornecedorCreate):
    service = FornecedorService()
    updated_fornecedor = service.update_fornecedor(id, fornecedor)
    if not updated_fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return updated_fornecedor


@router.delete("/{id}/")
def delete_fornecedor(id: int):
    service = FornecedorService()
    result = service.delete_fornecedor(id)
    if "não encontrado" in result.get("message", ""):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result
