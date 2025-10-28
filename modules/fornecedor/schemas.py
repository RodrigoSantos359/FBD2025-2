from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    ATIVO = "ATIVO"
    INATIVO = "INATIVO"
    SUSPENSO = "SUSPENSO"

class FornecedorBase(BaseModel):
    nome: str
    cnpj: str
    status: StatusEnum
    empresa_id: int

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int

    class Config:
        orm_mode = True
