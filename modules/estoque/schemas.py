from pydantic import BaseModel

class EstoqueBase(BaseModel):
    produto_id: int
    quantidade: int
    

class EstoqueCreate(BaseModel):
    produto_id: int
    quantidade: int

class Estoque(EstoqueBase):
    id: int
    

    class Config:
        orm_mode = True  # importante para serializar objetos SQLAlchemy    
