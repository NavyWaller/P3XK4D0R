from app.services.openrouter_service import analyze_topic

async def risk_agent(topic: str):

    prompt = f"""
    Identify risks and threat vectors related to:

    {topic}

    Focus on:
    - cyber threats
    - misinformation
    - strategic instability
    - emerging security risks

    Keep response concise and intelligence-oriented.
    """

    result = await analyze_topic(prompt)

    return result