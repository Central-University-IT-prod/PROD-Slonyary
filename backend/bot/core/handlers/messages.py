from aiogram.types import Message


async def message_handler(message: Message):
    """
    Обработка сообщений
    """

    print(message)

    await message.answer('test')
