import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from sqlalchemy.ext.asyncio import AsyncSession

from core.utils.keyboards import ready_keyboard
from core.utils.messages import BotText

from core.settings.config import TOKEN

from core.handlers.logger import TgLogger

from shared.database.models import User

tg_log = TgLogger()
bot: Bot = Bot(TOKEN)


async def start_handler(message: Message, command: CommandObject, user: User, session: AsyncSession):
    """
    Команда /start
    """

    # Извлекаем данные переданные в команду
    deeplink = command.args

    # if isinstance(deeplink, str) and deeplink.startswith('invite'):
    #     channel_id, role = deeplink.replace('invite', '').split('_')
    #
    #     ...

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
