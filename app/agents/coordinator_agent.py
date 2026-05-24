import asyncio
import uuid

from app.agents.search_agent import search_agent
from app.services.web_fetcher import fetch_web_content
from app.agents.geopolitical_agent import geopolitical_agent
from app.agents.technical_agent import technical_agent
from app.agents.risk_agent import risk_agent
from app.agents.source_scoring_agent import source_scoring_agent
from app.agents.synthesis_agent import synthesis_agent
from app.services.embedding_service import create_embedding
from app.services.firestore_service import save_report_metadata
from app.services.pdf_generator import generate_pdf_report

# Memory in Pinecone
from app.memory.pinecone_memory import (
        store_memory, 
        search_memory  
)

async def coordinator_agent(topic: str):

    # SEMANTIC MEMORY RETRIEVAL
    
    topic_embedding = await create_embedding(topic)

    #Memory in Pinecone
    similar_memories = search_memory(
        topic_embedding
    )
    
    matches = similar_memories.get("matches", [])

    memory_chunks = []

    for match in matches:

        metadata = match.get("metadata", {})

        summary = metadata.get("summary", "")

        if summary:
            memory_chunks.append(summary)

    memory_context = "\n\n".join(memory_chunks)

    # SEARCH
    trusted_domains = [
        "reuters.com", 
        "cnn.com"
    ]

    search_data = search_agent(
        topic,
        trusted_domains=trusted_domains
    )

    if "error" in search_data:
        return {
            "topic": topic,
            "search_error": search_data["error"]
        }

    search_results = search_data["results"]

    top_urls = [
        r["url"]
        for r in search_results
        if r.get("url")
    ][:3]

    # FETCH WEB CONTENT
    web_tasks = [
        fetch_web_content(url)
        for url in top_urls
    ]

    web_contents = await asyncio.gather(
        *web_tasks,
        return_exceptions=True
    )

    extracted_pages = []

    combined_content = ""

    for url, content in zip(top_urls, web_contents):

        if isinstance(content, Exception):

            extracted_pages.append({
                "url": url,
                "error": str(content)
            })

        else:

            extracted_pages.append({
                "url": url,
                "content_preview": content[:1000]
            })

            combined_content += f"\n\nSOURCE: {url}\n{content[:3000]}"

    # SPECIALIZED ANALYSIS
    geo_task = geopolitical_agent(topic)
    tech_task = technical_agent(topic)
    risk_task = risk_agent(topic)

    geo, tech, risk = await asyncio.gather(
        geo_task,
        tech_task,
        risk_task
    )

    # SOURCE SCORING
    scoring_tasks = [
        source_scoring_agent(content[:3000])
        for content in web_contents
        if not isinstance(content, Exception)
    ]

    source_scores = await asyncio.gather(*scoring_tasks)

    # FINAL SYNTHESIS using the source quality assessment
    formatted_scores = "\n\n".join(source_scores)

    synthesis = await synthesis_agent(
        topic,
        combined_content + "\n\nSEMANTIC MEMORY:\n" + memory_context,
        formatted_scores
    )

    # Store semantic memory for future reports

    summary_embedding = await create_embedding(synthesis)
    store_memory(
        topic=topic,
        summary=synthesis,
        embedding=summary_embedding
    )
   
    # Final Intelligence Report generation (PDF)

    pdf_path = generate_pdf_report(
        topic=topic,
        synthesis=synthesis,
        geopolitical=geo,
        technical=tech,
        risk=risk,
        sources=search_results
    )

    # Write report metadata in FireStore
    try:
        save_report_metadata({
            "topic": topic,
            "pdf_url": pdf_path
        })
    except Exception as e:
        print("🔥 FIRESTORE ERROR")
        print(str(e))
    
    return {
        "topic": topic,
        "search_results": search_results,
        "extracted_pages": extracted_pages,
        "source_evaluations": source_scores,
        "geopolitical_analysis": geo,
        "technical_analysis": tech,
        "risk_analysis": risk,
        "final_synthesis": synthesis,
        "pdf_report": f"{pdf_path}"
    }