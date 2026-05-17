from app.agents.research_agent import research_agent

async def coordinator_agent(topic: str):

    research = await research_agent(topic)

    return {
        "topic": topic,
        "research": research
    }