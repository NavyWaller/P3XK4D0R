import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="p3xk4d0r_memory"
)


def store_memory(
    doc_id,
    topic,
    summary,
    embedding
):

    collection.add(
        ids=[doc_id],
        documents=[summary],
        metadatas=[{
            "topic": topic
        }],
        embeddings=[embedding]
    )


def search_similar_memories(
    embedding,
    n_results=3
):

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results