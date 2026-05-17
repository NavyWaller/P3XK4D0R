from app.services.web_fetcher import fetch_web_content

async def source_agent(url: str):

    content = await fetch_web_content(url)

    return {
        "url": url,
        "content": content
    }