from app.services.openrouter_service import analyze_topic

async def source_scoring_agent(source_text: str):

    prompt = f"""
    Evaluate this OSINT source.

    Assess:
    - credibility
    - relevance
    - technical value
    - geopolitical significance
    - possible bias

    Return:
    - credibility score (1-10)
    - short assessment

    Source content:

    {source_text[:4000]}
    """

    result = await analyze_topic(prompt)

    return result