from typing import Optional

from fastapi import APIRouter

from modules.fornecedor import schemas
from modules.fornecedor.schemas import FornecedorCreate
from modules.fornecedor.service import FornecedorService

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@router.get("/", response_model=list[schemas.Fornecedor])
def list_fornecedores():
    return FornecedorService().listar_fornecedores()

@router.get("/{id}/", response_model=Optional[schemas.Fornecedor])
def get_fornecedor_by_id(id: int):
    return FornecedorService().buscar_fornecedor_por_id(id)

@router.post("/", response_model=schemas.Fornecedor)
def add_fornecedor(fornecedor: schemas.FornecedorCreate):
    return FornecedorService().criar_fornecedor(fornecedor)
