from pydantic import BaseModel

class TipoBase(BaseModel):
    nome: str
    cod_tipo: str
    empresa_id: int

class TipoCreate(TipoBase):
    pass

class Tipo(TipoBase):
    id: int
    class Config:
        orm_mode = True