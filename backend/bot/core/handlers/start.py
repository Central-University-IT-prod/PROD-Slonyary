from aiogram.filters import CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from core.utils.keyboards import reply_keyboard


async def start_handler(message: Message, command: CommandObject):
    """
    Команда /start
    """

    # Извлекаем данные переданные в команду
    deeplink = command.args

    await message.answer('Нажмите кнопку ниже и выберите канал', reply_markup=reply_keyboard)
