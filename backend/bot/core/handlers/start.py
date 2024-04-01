import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from core.utils.keyboards import ready_keyboard
from core.utils.messages import BotText

from core.settings.config import TOKEN

from core.handlers.logger import Logger

from core.services.database import get_user, add_user

log = Logger()
bot: Bot = Bot(TOKEN)


async def start_handler(message: Message, command: CommandObject):
    """
    Команда /start
    """

    # Извлекаем данные переданные в команду
    deeplink = command.args

    if not await get_user(user_id=message.from_user.id):  # todo можно добавить кеширование redis
        await add_user(user_id=message.from_user.id,
                       name=message.from_user.first_name,
                       username=message.from_user.username)

        await log.message(text=f"Новый пользователь: {message.from_user.first_name}")  # todo убрать в проде

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
