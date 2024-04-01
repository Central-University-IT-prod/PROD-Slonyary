import asyncio

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from scheduler.utils.get_tg_posts_to_publish import get_tg_posts_to_publish
from shared.utils.publish_tg_post import publish_tg_post


async def tg_post_publisher(
    bot: Bot,
    session: AsyncSession,
    interval: float = 60.0,
) -> None:
    while True:
        posts_to_publish = await get_tg_posts_to_publish(session)
        for post in posts_to_publish:
            await publish_tg_post(post, bot)
        await asyncio.sleep(interval)
