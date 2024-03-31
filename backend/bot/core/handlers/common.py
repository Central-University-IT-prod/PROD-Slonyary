# Регистрация обработчиков
from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from .chat_shared import shared_handler
from .start import start_handler
from .messages import message_handler


async def register_main_handlers(router: Router) -> None:
    """
    Регистрация основных обработчиков
    """

    # Стартовая команда
    router.message.register(start_handler, CommandStart())
    router.message.register(shared_handler, F.chat_shared)
    router.message.register(message_handler)
