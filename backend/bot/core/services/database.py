import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from shared.database.models import TgChannel
from shared.database.session import db_session_manager


async def get_channel_by_id(channel_id: int):
    async with db_session_manager() as session:
        query = sa.select(TgChannel).where(TgChannel.channel_id == channel_id)
        return await session.scalar(query)