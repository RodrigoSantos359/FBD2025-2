from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from core.db import get_db
from modules.company import schemas
from modules.company.repository import CompanyRepository

class CompanyService:
    def get_companies(self, db: Session = Depends(get_db)):
        repository = CompanyRepository(db)
        return repository.get_all()

    def create_company(self, company: schemas.CompanyCreate, db: Session = Depends(get_db)) -> schemas.Company:
        repository = CompanyRepository(db)
        return repository.save(company)

    def get_company_id(self, id: int, db: Session = Depends(get_db)):
        repository = CompanyRepository(db)
        company = repository.get_id(id)
        return company

    def update_company(self, id: int, company: schemas.CompanyCreate, db: Session = Depends(get_db)) -> Optional[schemas.Company]:
        repository = CompanyRepository(db)
        return repository.update(id, company)

    def delete_company(self, id: int, db: Session = Depends(get_db)):
        repository = CompanyRepository(db)
        return repository.delete(id)