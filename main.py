from fastapi import FastAPI
from api.routes import company_routes

app = FastAPI()
app.include_router(company_routes.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
