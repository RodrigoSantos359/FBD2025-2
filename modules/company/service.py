from modules.company import schemas
from modules.company.repository import CompanyRepository


class CompanyService:
    def get_companies(self):
        repository = CompanyRepository()
        return repository.get_all()

    def create_company(self, company: schemas.CompanyCreate):
        # VALIDAR OS CAMPOS DO CREATE AQUI
        repository = CompanyRepository()
        return repository.save(company)

    def get_company_id(self, id: int):
        repository = CompanyRepository()
        company = repository.get_id(id)
        return company
