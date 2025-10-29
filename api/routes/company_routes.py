from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from core.db import DataBase
from core.db import get_db
from modules.company import schemas
from modules.company.schemas import CompanyCreate
from modules.company.service import CompanyService

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("/", response_model=list[schemas.Company])
def list_companies(db: DataBase = Depends(get_db)):
    service = CompanyService()
    return service.get_companies()


@router.get("/{id}/", response_model=Optional[schemas.Company])
def get_company_by_id(id: int, db: DataBase = Depends(get_db)):
    service = CompanyService()
    company = service.get_company_id(id)
    if not company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return company


@router.post("/", response_model=schemas.Company)
def create_company(company: CompanyCreate, db: DataBase = Depends(get_db)):
    service = CompanyService()
    return service.create_company(company)


@router.put("/{id}/", response_model=schemas.Company)
def update_company(id: int, company: CompanyCreate, db: DataBase = Depends(get_db)):
    service = CompanyService()
    updated_company = service.update_company(id, company)
    if not updated_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return updated_company


@router.delete("/{id}/")
def delete_company(id: int, db: DataBase = Depends(get_db)):
    service = CompanyService()
    result = service.delete_company(id)
    if "não encontrada" in result.get("message", ""):
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result