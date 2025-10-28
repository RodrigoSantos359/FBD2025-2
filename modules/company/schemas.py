from pydantic import BaseModel
from typing import Literal

StatusEnum = Literal['ATIVO', 'INATIVO', 'SUSPENSO']
class CompanyBase(BaseModel):
    nome: str
    cnpj: str
    status: StatusEnum

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True