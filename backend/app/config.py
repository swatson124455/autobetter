import os
import json
from pydantic import BaseSettings

class Settings(BaseSettings):
    WALLET_PRIVATE_KEY: str = ''
    POLYMARKET_API_KEY: str = ''
    POLL_INTERVAL: int = 10
    KELLY_FRACTION: float = 0.5
    DATABASE_URL: str = "sqlite+aiosqlite:///./data.db"
    INFURA_ID: str = ''
    class Config:
        env_file = '.env'

settings = Settings()

# Fallback: load wallet from wallet.json if ENV missing
if not settings.WALLET_PRIVATE_KEY:
    try:
        with open('wallet.json') as wf:
            data = json.load(wf)
            settings.WALLET_PRIVATE_KEY = data.get('privateKey', '')
    except FileNotFoundError:
        pass
