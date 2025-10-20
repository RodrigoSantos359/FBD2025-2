from pydantic import BaseModel

class FornecedorBase(BaseModel):
    nome: str
    cnpj: str
    status: bool
    empresa_id: int

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int
    class Config:
        orm_mode = True
