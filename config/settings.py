from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import urllib

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="Lecton AI Core Engine")
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)

    VECTOR_DB_PROVIDER: str = Field(default="pgvector")
    
    DB_USER: str = Field(default="postgres")
    DB_PASSWORD: str = Field(default="Admin@123")
    DB_HOST: str = Field(default="127.0.0.1")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="lecton_ai_db")
    
    @property
    def DATABASE_URL(self) -> str:
        safe_password = urllib.parse.quote_plus(self.DB_PASSWORD)
        
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{safe_password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()