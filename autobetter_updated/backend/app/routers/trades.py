from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.poller import AsyncSessionLocal
from app.models import Trade
from sqlalchemy import select

router = APIRouter()

@router.get('/trades')
async def read_trades():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Trade))
        return result.scalars().all()
