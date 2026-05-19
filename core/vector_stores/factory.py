import logging

from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from core.vector_stores import BaseVectorStore, PGVectorStore, ChromaVectorStore, PineconeVectorStore
from core.vector_stores import QdrantVectorStore

class VectorStoreFactory:

    def get_vector_store(db_session: AsyncSession = None) -> BaseVectorStore:
        provider = settings.VECTOR_DB_PROVIDER.lower()

        match provider:
            case "pgvector":
                return PGVectorStore(session=db_session)
            case "chroma":
                return ChromaVectorStore(
                    host=getattr(settings, "CHROMA_HOST", "localhost"),
                    port=getattr(settings, "CHROMA_PORT", 8000)
                )
            case "pinecone":
                return PineconeVectorStore(
                    api_key=getattr(settings, "PINECONE_API_KEY", "")
                )
            case "qdrant":
                return QdrantVectorStore(
                    url=getattr(settings, "QDRANT_URL", "http://localhost:6333"),
                    api_key=getattr(settings, "QDRANT_API_KEY", "")
                )
            case _:
                raise NotImplementedError("Vector DB not found")



