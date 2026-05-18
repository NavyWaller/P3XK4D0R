import asyncio

from app.agents.search_agent import search_agent
from app.agents.web_fetcher import fetch_web_content
from app.agents.geopolitical_agent import geopolitical_agent
from app.agents.technical_agent import technical_agent
from app.agents.risk_agent import risk_agent


async def coordinator_agent(topic: str):

    # 1. buscar fuentes
    search_results = search_agent(topic)

    top_urls = [r["url"] for r in search_results[:3]]

    # 2. extraer contenido web
    web_tasks = [fetch_web_content(url) for url in top_urls]
    web_contents = await asyncio.gather(*web_tasks)

    # 3. análisis paralelo
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
        "sources": search_results,
        "web_extracted": web_contents,
        "geopolitical": geo,
        "technical": tech,
        "risk": risk
    }