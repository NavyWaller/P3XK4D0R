import os

from pinecone import Pinecone


pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    host=os.getenv("PINECONE_INDEX_HOST")
)

def store_embedding(
    vector_id,
    embedding,
    metadata
):

    index.upsert([
        {
            "id": vector_id,
            "values": embedding,
            "metadata": metadata
        }
    ])

def semantic_search(
    embedding,
    top_k=5
):

    return index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True
    )

