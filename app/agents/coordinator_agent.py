from app.agents.geopolitical_agent import geopolitical_agent
from app.agents.technical_agent import technical_agent
from app.agents.risk_agent import risk_agent
from app.agents.source_agent import source_agent

import asyncio

async def coordinator_agent(topic: str):

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
        "geopolitical": geo,
        "technical": tech,
        "risk": risk,
        "note": "web ingestion layer ready (next phase)"
    }