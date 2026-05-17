import asyncio

from app.agents.geopolitical_agent import geopolitical_agent
from app.agents.technical_agent import technical_agent
from app.agents.risk_agent import risk_agent

async def coordinator_agent(topic: str):

    geopolitical_task = geopolitical_agent(topic)
    technical_task = technical_agent(topic)
    risk_task = risk_agent(topic)

    geopolitical, technical, risk = await asyncio.gather(
        geopolitical_task,
        technical_task,
        risk_task
    )

    return {
        "topic": topic,
        "geopolitical_analysis": geopolitical,
        "technical_analysis": technical,
        "risk_analysis": risk
    }