import asyncio

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from scheduler.utils.get_posts_to_publish import get_posts_to_publish
from shared.core.enums import PostStatus
from shared.utils.publish_tg_post import publish_tg_post

# from shared.utils.publish_vk_post import publish_vk_post


async def post_publisher(
    bot: Bot,
    session: AsyncSession,
    interval: float = 60.0,
) -> None:
    while True:
        posts_to_publish = await get_posts_to_publish(session)
        for post in posts_to_publish:
            await publish_tg_post(post, bot, session)
            # await publish_vk_post(post)

            post.status = PostStatus.published
            await session.commit()

        await asyncio.sleep(interval)
