from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from core.database.session import init_db_extensions, async_engine  # ◄ Bỏ chữ src.

@asynccontextmanager
async def app_lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await init_db_extensions()
    yield
    await async_engine.dispose()