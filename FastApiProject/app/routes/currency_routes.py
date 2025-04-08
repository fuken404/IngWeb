from fastapi import APIRouter, Query
from app.services.currency_service import convert_currency

router = APIRouter(prefix="/currency", tags=["Currency"])

@router.get("/convert")
async def convert(from_currency: str = Query(...), to_currency: str = Query(...), amount: float = Query(...)):
    return await convert_currency(from_currency, to_currency, amount)
