import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


async def create_embedding(text: str):

    url = "https://openrouter.ai/api/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "text-embedding-3-small",
        "input": text[:8000]
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

    data = response.json()

    return data["data"][0]["embedding"]