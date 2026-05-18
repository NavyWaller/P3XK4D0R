import asyncio

from app.agents.search_agent import search_agent
from app.services.web_fetcher import fetch_web_content

from app.agents.geopolitical_agent import geopolitical_agent
from app.agents.technical_agent import technical_agent
from app.agents.risk_agent import risk_agent


async def coordinator_agent(topic: str):

    # SEARCH
    search_data = search_agent(topic)

    if "error" in search_data:

        return {
            "topic": topic,
            "search_error": search_data["error"]
        }

    search_results = search_data["results"]

    # URLS
    top_urls = [
        r["url"]
        for r in search_results
        if r.get("url")
    ][:3]

    # FETCH
    web_tasks = [
        fetch_web_content(url)
        for url in top_urls
    ]

    web_contents = await asyncio.gather(
        *web_tasks,
        return_exceptions=True
    )

    extracted_pages = []

    for url, content in zip(top_urls, web_contents):

        if isinstance(content, Exception):

            extracted_pages.append({
                "url": url,
                "error": str(content)
            })

        else:

            extracted_pages.append({
                "url": url,
                "content_preview": content[:1000]
            })

    # AGENTS
    geo_task = geopolitical_agent(topic)
    tech_task = technical_agent(topic)
    risk_task = risk_agent(topic)

    geo, tech, risk = await asyncio.gather(
        geo_task,
        tech_task,
        risk_task
    )

    return {
        "topic": topic,
        "search_results": search_results,
        "extracted_pages": extracted_pages,
        "geopolitical_analysis": geo,
        "technical_analysis": tech,
        "risk_analysis": risk
    }