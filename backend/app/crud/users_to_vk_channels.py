import sqlalchemy as sa
from app.crud.base import CrudBase
from app.schemas import (
    TgChannelRead,
    TgChannelUpdate,
    UsersToVkChannelsCreate,
    VkChannelRead,
    VkChannelUpdate,
)
from shared.database.models import User, UsersToVkChannels, VkChannel
from sqlalchemy.ext.asyncio import AsyncSession


class CrudUsersToVkChannels(
    CrudBase[
        UsersToVkChannels,
        UsersToVkChannelsCreate,
        TgChannelRead,
        TgChannelUpdate,
    ]
):
    def __init__(self, db: AsyncSession):
        super().__init__(db, UsersToVkChannels)

    async def get_user_vk_channels(self, user: User) -> list[UsersToVkChannels]:
        query = sa.select(UsersToVkChannels).where(UsersToVkChannels.user_id == user.id)
        results = await self.db.scalars(query)
        result_channels = [user_to_vk_channel.channel for user_to_vk_channel in results]
        return result_channels

    async def is_user_access(self, user: User, vk_channel: VkChannel) -> bool:
        query = sa.select(UsersToVkChannels).where(
            UsersToVkChannels.user_id == user.id,
            UsersToVkChannels.channel_id == vk_channel.id,
        )
        result = await self.db.scalar(query)
        return bool(result)
