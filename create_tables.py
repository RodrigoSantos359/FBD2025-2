from core.db import Base, engine
from modules.company.models import Empresa
from modules.tipo.models import Tipo

# Create all tables in the database
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")