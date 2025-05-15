import asyncio
from app.config import settings
from app.services.scraper import fetch_markets
from app.services.strategy import generate_signals
from app.services.wallet import execute_trade
from app.models import Market, Trade, Base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(settings.DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def update_db(markets):
    async with AsyncSessionLocal() as session:
        for m in markets:
            obj = await session.get(Market, m['id'])
            if obj:
                obj.yes_prob = m['probabilities']['yes']
                obj.no_prob = m['probabilities']['no']
                obj.updated_at = m.get('updated_at', None)
            else:
                session.add(Market(
                    id=m['id'],
                    name=m['name'],
                    yes_prob=m['probabilities']['yes'],
                    no_prob=m['probabilities']['no']
                ))
        await session.commit()

async def poll_loop():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    while True:
        markets = await fetch_markets()
        await update_db(markets)
        signals = await generate_signals(markets)
        for sig in signals:
            trade = await execute_trade(sig)
            async with AsyncSessionLocal() as session:
                session.add(Trade(
                    market_id=trade['market_id'],
                    side=trade['side'],
                    amount=trade['amount'],
                    price=trade['price']
                ))
                await session.commit()
        await asyncio.sleep(settings.POLL_INTERVAL)

def start_poller():
    import threading
    threading.Thread(target=lambda: asyncio.run(poll_loop()), daemon=True).start()
