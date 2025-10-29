from fastapi import Depends
from core.db import DataBase, get_db
from modules.company import schemas
from modules.company.repository import CompanyRepository

class CompanyService:
    def get_companies(self, db: DataBase = Depends(get_db)):
        repository = CompanyRepository()
        return repository.listar()

    def create_company(self, company: schemas.CompanyCreate, db: DataBase = Depends(get_db)):
        repository = CompanyRepository()
        return repository.criar(company)

    def get_company_id(self, id: int, db: DataBase = Depends(get_db)):
        repository = CompanyRepository()
        company = repository.buscar_por_id(id)
        return company

    def update_company(self, id: int, company: schemas.CompanyCreate, db: DataBase = Depends(get_db)):
        repository = CompanyRepository()
        return repository.atualizar(id, company)

    def delete_company(self, id: int, db: DataBase = Depends(get_db)):
        repository = CompanyRepository()
        return repository.deletar(id)