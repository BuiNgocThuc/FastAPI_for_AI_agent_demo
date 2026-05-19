# core/vectorstores/chroma.py
from typing import List, Dict, Any
# Yêu cầu cài: pip install chromadb
import chromadb

from core.vector_stores import BaseVectorStore


class ChromaVectorStore(BaseVectorStore):
    def __init__(self, host: str, port: int, collection_name: str = "lecton_knowledge"):
        self.host = host
        self.port = port
        self.client = chromadb.HttpClient(host=host, port=port)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    async def add_vector(self, doc_id: int, content: str, embedding: List[float]) -> bool:
        self.collection.add(ids=[str(doc_id)], embeddings=[embedding], documents=[content])
        return True

    async def similarity_search(self, embedding: List[float], limit: int = 3) -> List[Dict[str, Any]]:
        return [{"id": "chroma-1", "content": "Dữ liệu Chroma mượt mà", "distance": 0.1}]