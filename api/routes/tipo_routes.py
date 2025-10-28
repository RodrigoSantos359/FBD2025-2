from typing import Optional

from fastapi import APIRouter, HTTPException

from modules.tipo import schemas
from modules.tipo.schemas import TipoCreate
from modules.tipo.service import TipoService

router = APIRouter(prefix="/tipo", tags=["Tipo"])


@router.get("/", response_model=list[schemas.Tipo])
def list_tipos():
    service = TipoService()
    return service.get_tipos()


@router.get("/{id}/", response_model=Optional[schemas.Tipo])
def get_tipo_by_id(id: int):
    service = TipoService()
    tipo = service.get_tipo_id(id)
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")
    return tipo


@router.post("/", response_model=schemas.Tipo)
def create_tipo(tipo: TipoCreate):
    service = TipoService()
    return service.create_tipo(tipo)


@router.put("/{id}/", response_model=schemas.Tipo)
def update_tipo(id: int, tipo: TipoCreate):
    service = TipoService()
    updated_tipo = service.update_tipo(id, tipo)
    if not updated_tipo:
        raise HTTPException(status_code=404, detail="Tipo não encontrado")
    return updated_tipo


@router.delete("/{id}/")
def delete_tipo(id: int):
    service = TipoService()
    result = service.delete_tipo(id)
    if "não encontrado" in result.get("message", ""):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result



