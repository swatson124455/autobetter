import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    WALLET_PRIVATE_KEY: str
    POLYMARKET_API_KEY: str
    POLL_INTERVAL: int = 10
    KELLY_FRACTION: float = 0.5
    DATABASE_URL: str = "sqlite+aiosqlite:///./data.db"
    INFURA_ID: str
    class Config:
        env_file = '.env'

settings = Settings()
