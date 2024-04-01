import sqlalchemy as sa
from app.crud.base import CrudBase
from app.schemas import TgChannelRead, TgChannelUpdate, User, UsersToTgChannelsCreate
from shared.database.models import TgChannel, UsersToTgChannels
from sqlalchemy.ext.asyncio import AsyncSession


class CrudUsersToTgChannels(
    CrudBase[
        UsersToTgChannels,
        UsersToTgChannelsCreate,
        TgChannelRead,
        TgChannelUpdate,
    ]
):
    def __init__(self, session: AsyncSession):
        super().__init__(session, UsersToTgChannels)

    async def get_user_tg_channels(self, user: User) -> list[UsersToTgChannels]:
        query = sa.select(UsersToTgChannels).where(UsersToTgChannels.user_id == user.id)
        results = await self.session.scalars(query)
        result_channels = [
            user_to_tg_channel.tg_channel for user_to_tg_channel in results
        ]
        return result_channels

    async def is_user_access(self, user: User, tg_channel: TgChannel) -> bool:
        query = sa.select(UsersToTgChannels).where(
            UsersToTgChannels.user_id == user.id,
            UsersToTgChannels.tg_channel_id == tg_channel.id,
        )
        result = await self.session.scalar(query)
        return bool(result)
