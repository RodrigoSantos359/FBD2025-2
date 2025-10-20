from typing import Optional

from fastapi import APIRouter

from modules.company import schemas
from modules.company.schemas import CompanyCreate
from modules.company.service import CompanyService

# from app.modules.company import service, schemas

router = APIRouter(prefix="/company", tags=["Company"])


@router.get("/", response_model=list[schemas.Company])
def list_companies():
    service = CompanyService()
    return service.get_companies()
    # return service.get_companies()


@router.get("/{id}/", response_model=Optional[schemas.Company])
def get_company_by_id(id: int):
    service = CompanyService()
    return service.get_company_id(id)


@router.post("/", response_model=dict)
def create_company(company: CompanyCreate):
    print("Dados recebidos:", company.dict())  # Log para depuração
    service = CompanyService()
    return service.create_company(company)
