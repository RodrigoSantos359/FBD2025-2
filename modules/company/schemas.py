from pydantic import BaseModel

class Company(BaseModel):
    id: int
    name: str

class CompanyCreate(BaseModel):
    cnpj: str
    name: str
