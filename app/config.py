from pydantic_settings import BaseSettings
from pathlib import Path

# Construct a path to the .env file in the root directory (RAG IMPLEMENTATION)
# This ensures the settings are loaded correctly regardless of where the script is run from.


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()