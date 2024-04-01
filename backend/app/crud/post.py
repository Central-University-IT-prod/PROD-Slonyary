import sqlalchemy as sa
from app.crud.base import CrudBase
from app.schemas import PostCreate, PostRead, PostUpdate
from shared.database.models import (
    Post,
    PostsToTgChannels,
    PostsToVkChannels,
    TgChannel,
    User,
    UsersToTgChannels,
    UsersToVkChannels,
    VkChannel,
)
from sqlalchemy.ext.asyncio import AsyncSession


class CrudPost(CrudBase[Post, PostCreate, PostRead, PostUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Post)

    async def create(self, obj_in: PostCreate) -> Post:
        db_obj = Post(
            owner_id=obj_in.owner_id,
            html_text=obj_in.html_text,
            plain_text=obj_in.plain_text,
            publish_time=obj_in.publish_time,
            is_published=False,
            status=obj_in.status,
        )
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def is_user_access(self, user: User, post: Post) -> bool:
        """Check if user has access to post."""
        print(user.tg_channels)
        for post_tg_channel in post.tg_channels:
            print(post_tg_channel.id)
            if post_tg_channel in user.tg_channels:
                return True

        for post_vk_channel in post.vk_channels:
            if post_vk_channel in user.vk_channels:
                return True

        return False
