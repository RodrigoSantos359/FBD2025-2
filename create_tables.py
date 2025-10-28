from core.db import Base, engine
from modules.company.models import Empresa
from modules.tipo.models import Tipo
from modules.fornecedor.models import Fornecedor
from modules.produto.models import Produto
from modules.estoque.models import Estoque

# Create all tables in the database
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")

# Test model resolution
from sqlalchemy.exc import InvalidRequestError

def test_model_resolution():
    try:
        print("Testing model resolution...")
        from modules.fornecedor.models import Fornecedor
        from modules.company.models import Empresa
        print("Fornecedor and Empresa models resolved successfully.")
    except InvalidRequestError as e:
        print(f"Model resolution failed: {e}")

test_model_resolution()