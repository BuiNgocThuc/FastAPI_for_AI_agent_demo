# core/vectorstores/qdrant.py
from typing import List, Dict, Any
# Yêu cầu cài: pip install qdrant-client
from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import PointStruct


from core.vector_stores import BaseVectorStore


class QdrantVectorStore(BaseVectorStore):
    def __init__(self, url: str, api_key: str, collection_name: str = "lecton_knowledge"):
        self.url = url
        self.api_key = api_key
        self.collection_name = collection_name
        self.client = AsyncQdrantClient(url=url, api_key=api_key)


    async def add_vector(self, doc_id: int, content: str, embedding: List[float]) -> bool:
        # Giả lập logic gọi Qdrant
        await self.client.upsert(
            collection_name=self.collection_name,
            points=[PointStruct(id=doc_id, vector=embedding, payload={"content": content})]
        )
        return True

    async def similarity_search(self, embedding: List[float], limit: int = 3) -> List[Dict[str, Any]]:
        # Giả lập kết quả trả về từ Qdrant
        return [{"id": "qdrant-1", "content": "Dữ liệu Qdrant siêu tốc", "score": 0.99}]