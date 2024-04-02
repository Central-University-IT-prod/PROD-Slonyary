import asyncio
import logging

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from scheduler.utils.get_posts_to_publish import get_posts_to_publish
from shared.utils.publish_tg_post import (
    mark_post_as_published,
    notify_owner_about_publish,
    publish_tg_post,
)

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

            logging.info(f"Отправил пост {post.id}")
            await mark_post_as_published(post, session)
            logging.info(f"Отметил пост {post.id} опубликованным")
            await notify_owner_about_publish(post, bot)
            logging.info(f"Сообщил создателю поста {post.id} о публикации")

        await asyncio.sleep(interval)
