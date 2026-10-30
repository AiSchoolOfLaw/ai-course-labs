# Add to server.py (A6), below the existing tools
from rag import col, ingest

ingest()  # load the client documents into the index once, when the server starts

@mcp.tool()
def search_knowledge(question: str, k: int = 3) -> list[dict]:
    """Search the client's documents. Returns passages with their source. Read-only."""
    res = col.query(query_texts=[question], n_results=k)
    return [{'source': m['source'], 'text': d}
            for d, m in zip(res['documents'][0], res['metadatas'][0])]
