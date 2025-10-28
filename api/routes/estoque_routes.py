from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from modules.estoque import schemas
from modules.estoque.schemas import EstoqueCreate
from modules.estoque.service import EstoqueService

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.get("/estoques/", response_model=list[schemas.Estoque])
def list_estoques(db: Session = Depends(get_db)):
    return EstoqueService(db).listar_estoques()


@router.get("/estoques/{id}/", response_model=Optional[schemas.Estoque])
def get_estoque_by_id(id: int, db: Session = Depends(get_db)):
    estoque = EstoqueService(db).listar_estoque_por_id(id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque


@router.post("/estoques/", response_model=schemas.Estoque)
def create_estoque(estoque: EstoqueCreate, db: Session = Depends(get_db)):
    # Removido o try/except para expor o traceback no console
    try:
        return EstoqueService(db).criar_estoque(estoque)
    except ValueError as e:
        # Mantido o tratamento de ValueError (Produto não encontrado)
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/estoques/{id}/", response_model=schemas.Estoque)
def update_estoque(id: int, estoque: EstoqueCreate, db: Session = Depends(get_db)):
    updated_estoque = EstoqueService(db).atualizar_estoque(id, estoque)
    if not updated_estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return updated_estoque


@router.delete("/estoques/{id}/")
def delete_estoque(id: int, db: Session = Depends(get_db)):
    result = EstoqueService(db).delete_estoque(id)
    if "não encontrado" in result.get("message", ""):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result


