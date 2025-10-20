from typing import Optional

from fastapi import APIRouter

from modules.tipo.schemas import Tipo, TipoCreate, TipoBase
from modules.tipo.service import TipoService

router = APIRouter(prefix="/tipo", tags=["Tipo"])


@router.get("/", response_model=list[Tipo])
def list_tipos():
    service = TipoService()
    return service.listar_tipos()


@router.get("/{id}/", response_model=Optional[Tipo])
def get_tipo_by_id(id: int):
    service = TipoService()
    return service.buscar_tipo_por_id(id)


@router.post("/with_id", response_model=Tipo)
def add_tipo(tipo: TipoBase):
    service = TipoService()
    return service.criar_tipo_com_id(tipo)