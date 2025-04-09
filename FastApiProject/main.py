from fastapi import FastAPI
from app.routes import item_routes, currency_routes

app = FastAPI()

app.include_router(item_routes.router)
app.include_router(currency_routes.router)
