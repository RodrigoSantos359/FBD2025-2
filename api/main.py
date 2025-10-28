from fastapi import FastAPI
from api.routes.company_routes import router as company_router
from api.routes.tipo_routes import router as tipo_router
from api.routes.fornecedor_routes import router as fornecedor_router
from api.routes.produto_routes import router as produto_router
from api.routes.estoque_routes import router as estoque_router

app = FastAPI(title="Sistema de Estoque")

app.include_router(company_router)
app.include_router(tipo_router)
app.include_router(fornecedor_router)
app.include_router(produto_router)
app.include_router(estoque_router)