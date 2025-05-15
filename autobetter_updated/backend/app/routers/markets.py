from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.app.services.poller import AsyncSessionLocal
from app.models import Market
from sqlalchemy import select

router = APIRouter()

@router.get('/markets')
async def read_markets():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Market))
        return result.scalars().all()
