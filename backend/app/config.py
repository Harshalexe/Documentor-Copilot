from pathlib import Path
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

_BACKEND_DIR = Path(__file__).resolve().parent.parent

# BaseSettings automatically aggregates configuration settings from multiple sources at the same time, following a strict
# hierarchy. By default, it prioritizes sources in this order: 
# 1. Explicit arguments passed directly when initializing the class.
# 2. Actual System Environment Variables (the ones set on your operating system or server).
# 3. Environment variables inside a .env file.
# 4. Default values written directly in your Python code.This means you can keep a .env file locally, 
# but the moment you deploy to a server (like Docker or AWS), you can use native system environment variables without changing a single line of your code.

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = _BACKEND_DIR / ".env",
        env_file_encoding = "utf-8",
        extra = "ignore",
    )

    supabase_url: str # so this all :str, :int will make pydantic to find the value from the environment variable and validate it and put it here.
    supabase_anon_key: str
    supabase_service_role_key: str
    database_url:str

    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-small"
    openai_embedding_dimensions: int = 1536 

    allowed_origins: str = "http://localhost:5173"

    @computed_field
    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip() for origin in self.allowed_origins.split(",")
            if origin.strip()
        ]


settings = Settings()