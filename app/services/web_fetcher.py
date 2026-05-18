import httpx
import trafilatura

async def fetch_web_content(url: str):

    headers = {
        "User-Agent": "Mozilla/5.0 (P3XK4D0R OSINT Bot)"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=headers,
            timeout=30
        )

    downloaded = response.text

    extracted_text = trafilatura.extract(
        downloaded,
        include_links=False,
        include_images=False
    )

    if not extracted_text:
        return "No meaningful content extracted."

    return extracted_text[:12000]