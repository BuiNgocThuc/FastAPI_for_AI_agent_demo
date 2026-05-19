from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from modules.documents.interfaces import IDocumentRepository
from modules.documents.models import DocumentModel
from shared.enums import DocumentStatus


class DocumentRepository(IDocumentRepository):

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def save(self, title: str) -> DocumentModel:

        entity = DocumentModel(title=title, status=DocumentStatus.PROCESSING)
        self.db.add(entity)

        await self.db.flush()
        return entity

    async def save_vector_chunk(self, doc_id: int, content: str, embedding: list[float]):
        query = text("""
                     INSERT INTO document_chunks (document_id, content, embedding)
                     VALUES (:doc_id, :content, :embedding);
                     """)
        try:
            await self.db.execute(query, {"doc_id": doc_id, "content": content, "embedding": str(embedding)})
        except Exception:
            pass
