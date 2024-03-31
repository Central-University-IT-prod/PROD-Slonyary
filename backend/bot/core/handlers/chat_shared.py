from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

from core.settings.config import TOKEN

bot: Bot = Bot(TOKEN)


async def shared_handler(message: Message):
    """
    Обработка чата, которым поделились
    """

    chat_shared_id: int = message.chat_shared.chat_id

    try:
        chat_info = await bot.get_chat(chat_id=chat_shared_id)
    except TelegramBadRequest:
        await message.answer('❌ Добавьте бота в канал!')
        return

    await message.answer('✅ Получено!')

    print(chat_info)
