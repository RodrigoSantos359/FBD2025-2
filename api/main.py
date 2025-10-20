from fastapi import FastAPI
from api.routes.company_routes import router as company_router
from api.routes.tipo_routes import router as tipo_router
from api.routes.fornecedor_routes import router as fornecedor_router

app = FastAPI(title="Sistema de Empresas")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Sistema de Empresas!"}

app.include_router(company_router)
app.include_router(tipo_router)
app.include_router(fornecedor_router)
