from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.database.session import async_session_factory 
from core.vector_stores.pgvector import PGVectorStore   

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def get_vector_store(db: AsyncSession = Depends(get_db)) -> PGVectorStore:
    return PGVectorStore(session=db)