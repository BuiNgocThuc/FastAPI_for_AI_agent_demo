# core/vectorstores/pinecone.py
from typing import List, Dict, Any

from pinecone import Pinecone

from core.vector_stores import BaseVectorStore
# Yêu cầu cài: pip install pinecone-client

class PineconeVectorStore(BaseVectorStore):
    def __init__(self, api_key: str, index_name: str = "lecton-index"):
        self.api_key = api_key
        pc = Pinecone(api_key=api_key)
        self.index = pc.Index(index_name)

    async def add_vector(self, doc_id: int, content: str, embedding: List[float]) -> bool:
        self.index.upsert(vectors=[(str(doc_id), embedding, {"content": content})])
        return True

    async def similarity_search(self, embedding: List[float], limit: int = 3) -> List[Dict[str, Any]]:
        return [{"id": "pinecone-1", "content": "Dữ liệu Pinecone Enterprise", "score": 0.95}]