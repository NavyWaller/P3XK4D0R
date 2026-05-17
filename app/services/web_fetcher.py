import httpx
from bs4 import BeautifulSoup

async def fetch_web_content(url: str):

    headers = {
        "User-Agent": "Mozilla/5.0 (P3XK4D0R OSINT bot)"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30)

    html = response.text

    soup = BeautifulSoup(html, "lxml")

    # eliminar scripts y estilos
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text(separator=" ", strip=True)

    # limpieza básica
    clean_text = " ".join(text.split())

    return clean_text[:8000]