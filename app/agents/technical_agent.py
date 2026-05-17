from app.services.openrouter_service import analyze_topic

async def technical_agent(topic: str):

    prompt = f"""
    Analyze the technical aspects of:

    {topic}

    Focus on:
    - AI technologies
    - cyber implications
    - infrastructure
    - scalability
    - emerging technologies

    Keep response concise.
    """

    result = await analyze_topic(prompt)

    return result