from core.vector_stores import BaseVectorStore
from modules.documents.interfaces import IDocumentService
from modules.documents.repositories import DocumentRepository
from modules.documents.schemas import DocumentIngestRequest, DocumentResponse


class DocumentService(IDocumentService):
    def __init__(self, repository: DocumentRepository, vector_store: BaseVectorStore):
        self.repository = repository
        self.vector_store = vector_store

    async def ingest_document(self, request: DocumentIngestRequest) -> DocumentResponse:
        doc_entity = await self.repository.save(title=request.title)

        # Giả lập băm nhỏ văn bản text -> tạo mảng số ma trận embedding
        mock_embedding = [0.15, -0.42, 0.88]

        await self.repository.save_vector_chunk(
            doc_id=doc_entity.id,
            content=request.content,
            embedding=mock_embedding
        )

        return DocumentResponse.model_validate(doc_entity)