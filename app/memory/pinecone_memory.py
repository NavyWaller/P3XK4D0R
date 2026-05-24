import os
import uuid

from pinecone import Pinecone


pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    host=os.getenv("PINECONE_INDEX_HOST")
)

def store_memory(
    topic,
    content,
    embedding,
    source_urls=None
):

    vector_id = str(uuid.uuid4())

    metadata = {
        "topic": topic,
        "content": content,
        "source_urls": source_urls or []
    }

    index.upsert(vectors=[
        {
            "id": vector_id,
            "values": embedding,
            "metadata": metadata
        }
    ])

def search_memory(
    embedding,
    top_k=5
):

    results = index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True
    )

    return results
