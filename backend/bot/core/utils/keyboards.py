from aiogram.types import KeyboardButton, KeyboardButtonRequestChat, ReplyKeyboardMarkup

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Добавить канал",
                request_chat=KeyboardButtonRequestChat(
                    request_id=1,
                    chat_is_channel=True,
                    bot_is_member=True,
                ),
            )
        ]
    ],
    is_persistent=True,
    resize_keyboard=True,
)
