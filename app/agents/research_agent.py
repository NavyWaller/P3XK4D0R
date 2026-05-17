from app.services.openrouter_service import analyze_topic

async def research_agent(topic: str):

    prompt = f"""
    Perform an OSINT-style preliminary research summary about:

    {topic}

    Focus on:
    - key actors
    - geopolitical relevance
    - technological implications
    - current strategic concerns

    Keep response concise.
    """

    result = await analyze_topic(prompt)

    return result