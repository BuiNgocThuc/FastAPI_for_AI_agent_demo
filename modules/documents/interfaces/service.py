from abc import ABC, abstractmethod
from modules.documents.schemas import DocumentIngestRequest, DocumentResponse

class IDocumentService(ABC):
    @abstractmethod
    async def ingest_document(self, request_dto: DocumentIngestRequest) -> DocumentResponse:
        pass