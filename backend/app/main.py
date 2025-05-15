from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.services.poller import start_poller

app = FastAPI()
import os

# Serve static frontend
app.mount("/", StaticFiles(directory="frontend_build", html=True), name="frontend")

@app.on_event('startup')
def on_startup():
    # Only start poller if all required settings present
    if settings.WALLET_PRIVATE_KEY and settings.POLYMARKET_API_KEY and settings.INFURA_ID:
        start_poller()

@app.get('/health')
def health():
    return {'status': 'ok'}
