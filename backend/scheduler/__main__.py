import asyncio
import contextlib

from aiogram import Bot
from aiogram.enums import ParseMode
from sqlalchemy.orm import close_all_sessions

from scheduler.tasks.publish import post_publisher
from shared.core.config import settings
from shared.database.session import db_session_manager


async def main() -> None:
    bot = Bot(
        token=settings.BOT_TOKEN,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    async with bot.context(), db_session_manager() as session:
        try:
            await post_publisher(bot, session, interval=60)
        finally:
            close_all_sessions()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
