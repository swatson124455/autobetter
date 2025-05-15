from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.services.poller import start_poller
from app.routers import markets, trades

app = FastAPI()
app.include_router(markets.router)
app.include_router(trades.router)
app.mount('/', StaticFiles(directory='../../frontend/build', html=True), name='frontend')

@app.on_event('startup')
def on_startup():
    start_poller()

@app.get('/health')
def health():
    return {'status': 'ok'}
