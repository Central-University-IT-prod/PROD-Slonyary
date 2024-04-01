import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase
from app.schemas import TgChannelRead, TgChannelUpdate, UsersToTgChannelsCreate
from shared.database.models import TgChannel, User, UsersToTgChannels


class CrudUsersToTgChannels(
    CrudBase[
        UsersToTgChannels,
        UsersToTgChannelsCreate,
        TgChannelRead,
        TgChannelUpdate,
    ]
):
    def __init__(self, db: AsyncSession):
        super().__init__(db, UsersToTgChannels)

    async def get_user_tg_channels(self, user: User) -> list[UsersToTgChannels]:
        query = sa.select(UsersToTgChannels).where(UsersToTgChannels.user_id == user.id)
        results = await self.db.scalars(query)
        result_channels = [user_to_tg_channel.channel for user_to_tg_channel in results]
        return result_channels

    async def is_user_access(self, user: User, tg_channel: TgChannel) -> bool:
        query = sa.select(UsersToTgChannels).where(
            UsersToTgChannels.user_id == user.id,
            UsersToTgChannels.channel_id == tg_channel.id,
        )
        result = await self.db.scalar(query)
        return bool(result)
