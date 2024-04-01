import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

from core.settings.config import TOKEN
from core.utils.messages import BotText
from core.utils.keyboards import ready_keyboard
from core.utils.keyboards import return_keyboard

from core.services.database import get_channel_by_id

bot: Bot = Bot(TOKEN)


async def shared_handler(message: Message):
    """
    Обработка чата, которым поделились
    """

    chat_shared_id: int = message.chat_shared.chat_id
    channel = await get_channel_by_id(chat_shared_id)

    if channel:

        return


    try:
        chat_info = await bot.get_chat(chat_id=chat_shared_id)
    except TelegramBadRequest:
        msg = await message.answer('❌')
        await asyncio.sleep(1)

        try:
            await msg.delete()
        except TelegramBadRequest:
            pass

        await message.answer(text=BotText.bot_kicked, parse_mode="HTML", reply_markup=ready_keyboard)
        return

    msg = await message.answer('🎉')
    await asyncio.sleep(1.7)

    try:
        await msg.delete()
    except TelegramBadRequest:
        pass

    await message.answer(text=BotText.added_channel, parse_mode="HTML", reply_markup=return_keyboard)

    print(chat_info)
    # todo: Добавление канала в базу данных, а также проверка на наличие канала в ней. (можно сделать фильтр)
