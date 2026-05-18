import logging
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config.settings import settings 

logger = logging.getLogger("core.database")

async_engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)
async_session_factory = async_sessionmaker(bind=async_engine, expire_on_commit=False)

async def init_db_extensions() -> None:
    async with async_engine.begin() as conn:
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        logger.info("Database extensions initialized.")
