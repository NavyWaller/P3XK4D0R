from app.services.openrouter_service import analyze_topic

async def geopolitical_agent(topic: str):

    prompt = f"""
    Analyze the geopolitical implications of:

    {topic}

    Focus on:
    - international actors
    - strategic competition
    - NATO relevance
    - global power balance

    Keep response concise and analytical.
    """

    result = await analyze_topic(prompt)

    return result