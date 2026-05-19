from abc import ABC, abstractmethod
from modules.documents.models import DocumentModel

class IDocumentRepository(ABC):
    @abstractmethod
    async def save(self, title: str) -> DocumentModel:
        pass

    @abstractmethod
    async def save_vector_chunk(self, doc_id: int, content: str, embedding: list[float]) -> None:
        pass