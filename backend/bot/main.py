import asyncio

from pyrogram import Client
from pyrogram.types import (ReplyKeyboardMarkup,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton)

from core.settings.config import TOKEN

# Create a client using your bot token
app = Client("my_bot", bot_token=TOKEN)


async def main():
    pass

if __name__ == '__main__':
    asyncio.run(main())