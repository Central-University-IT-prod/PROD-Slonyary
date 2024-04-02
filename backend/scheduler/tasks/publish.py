import asyncio
import contextlib

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from sqlalchemy.ext.asyncio import AsyncSession

from scheduler.utils.get_posts_to_publish import get_posts_to_publish
from shared.core.enums import PostStatus
from shared.database.models import Post
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

            await mark_post_as_published(post, session)
            await notify_owner_about_publish(post, bot)

        await asyncio.sleep(interval)


async def mark_post_as_published(post: Post, session: AsyncSession) -> None:
    post.status = PostStatus.published
    await session.commit()


async def notify_owner_about_publish(post: Post, bot: Bot) -> None:
    text = f"Пост №{post.id} опубликован!!!"
    with contextlib.suppress(TelegramAPIError):  # чтоб не сломалося
        await bot.send_message(chat_id=post.owner_id, text=text)
