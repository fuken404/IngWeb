import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # para cargar variables del archivo .env

ACCESS_KEY = os.getenv("CURRENCY_API_KEY")

async def convert_currency(from_currency: str, to_currency: str, amount: float):
    url = (
        f"https://api.exchangerate.host/convert"
        f"?from={from_currency}&to={to_currency}&amount={amount}&access_key={ACCESS_KEY}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": data.get("result"),
            "raw_response": data  # útil para depuración
        }
