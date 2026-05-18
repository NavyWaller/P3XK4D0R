from app.services.openrouter_service import analyze_topic

async def synthesis_agent(
    topic: str,
    combined_content: str,
    source_evaluations: str
):

    prompt = f"""
    Create an intelligence-style analytical briefing.

    TOPIC:
    {topic}

    SOURCE EVALUATIONS:
    {source_evaluations}

    SOURCE MATERIAL:
    {combined_content[:12000]}

    Instructions:
    - prioritize highly credible sources
    - mention possible bias or uncertainty
    - identify conflicting narratives
    - distinguish verified information from speculative claims

    Produce:
    - executive summary
    - key findings
    - strategic implications
    - technical implications
    - risk assessment
    - confidence level
    - future outlook

    Use concise intelligence-analysis style.
    """

    result = await analyze_topic(prompt)

    return result