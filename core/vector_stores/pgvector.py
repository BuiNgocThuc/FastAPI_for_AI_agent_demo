from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from core.vector_stores import BaseVectorStore


class PGVectorStore(BaseVectorStore):

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_vector(self, doc_id: int, content: str, embedding: List[float]) -> bool:
        query = text("""
            INSERT INTO document_chunks (document_id, content, embedding) 
            VALUES (:doc_id, :content, :embedding);
        """)
        
        try:
            await self.session.execute(query, {"doc_id": doc_id, "content": content, "embedding": str(embedding)})
            return True
        except Exception as e:
            print(f"Error adding vector: {e}")
            return False

    async def similarity_search(self, embedding: List[float], limit: int = 3) -> List[Dict[str, Any]]:
        query = text("""
            SELECT id, content, (embedding <=> :embedding) as distance 
            FROM document_chunks 
            ORDER BY embedding <=> :embedding 
            LIMIT :limit;
        """)

        try:
            result = await self.session.execute(query, {"embedding": str(embedding), "limit": limit})
            return [dict(row) for row in result.mappings()]
        except Exception:
            return []