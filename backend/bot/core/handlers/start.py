import asyncio

from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from core.utils.keyboards import ready_keyboard
from core.utils.messages import BotText


async def start_handler(message: Message, command: CommandObject):
    """
    Команда /start
    """

    # Извлекаем данные переданные в команду
    deeplink = command.args

    msg = await message.answer('⚡')
    await asyncio.sleep(1)

    try:
        await msg.edit_text(text=BotText.start.format(name=hbold(message.from_user.first_name)),
                            parse_mode="HTML",
                            reply_markup=ready_keyboard)
    except TelegramBadRequest:
        await message.answer(text=BotText.start.format(name=hbold(message.from_user.first_name)),
                             parse_mode="HTML",
                             reply_markup=ready_keyboard)
