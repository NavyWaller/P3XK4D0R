from app.services.openrouter_service import analyze_topic
from app.services.web_fetcher import fetch_web_content

async def research_agent(topic: str):

    prompt = f"""
    You are an OSINT research assistant.

    First, analyze the topic conceptually:

    {topic}

    Then provide structured intelligence insights.
    """

    result = await analyze_topic(prompt)

    return result