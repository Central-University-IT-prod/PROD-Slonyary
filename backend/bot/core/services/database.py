import traceback
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from shared.database.models import TgChannel, User, UsersToTgChannels
from shared.database.session import db_session_manager


class Roles:
    OWNER: str = "owner"
    MODERATOR: str = "moderator"
    EDITOR: str = "editor"


async def get_channel_by_id(channel_id: int):
    async with db_session_manager() as session:
        query = sa.select(TgChannel.id).where(TgChannel.id == channel_id)
        return await session.scalar(query)


async def add_channel(
    session: AsyncSession,
    channel_id: int,
    owner_id: int,
    title: str,
    subscribers: int = 0,
    description: Optional[str] = None,
    photo_url: Optional[str] = None,
    username: Optional[str] = None,
) -> bool:
    query = insert(TgChannel).values(
        id=channel_id,
        owner_id=owner_id,
        username=username,
        title=title,
        photo_url=photo_url,
        subscribers=subscribers,
        description=description
    )
    await session.execute(query)

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        print(traceback.format_exc())
        return False

    query = insert(UsersToTgChannels).values(
        user_id=owner_id,
        channel_id=channel_id,
        role=Roles.OWNER,
    )

    await session.execute(query)

    try:
        await session.commit()
    except IntegrityError:
        print(traceback.format_exc())
        await session.rollback()
        return False

    return True
