from typing import Optional

import sqlalchemy as sa

from shared.database.models import TgChannel, User
from shared.database.session import db_session_manager


async def get_user(user_id: int):
    async with db_session_manager() as session:
        query = sa.select(User.id).where(User.id == user_id)
        return await session.scalar(query)


async def add_user(user_id: int, name: str, username: Optional[str] = None):
    async with db_session_manager() as session:
        query = sa.insert(User).values(
            telegram_id=user_id, username=username, name=name
        )
        await session.execute(query)
        await session.commit()


async def get_channel_by_id(channel_id: int):
    async with db_session_manager() as session:
        query = sa.select(TgChannel.id).where(TgChannel.channel_id == channel_id)
        return await session.scalar(query)


async def add_channel(
    channel_id: int,
    owner_id: int,
    title: str,
    photo_url: Optional[str] = None,
    username: Optional[str] = None,
):
    async with db_session_manager() as session:
        query = sa.insert(TgChannel).values(
            channel_id=channel_id,
            owner_id=owner_id,
            username=username,
            title=title,
            photo_url=photo_url,
        )
        await session.execute(query)
        await session.commit()
