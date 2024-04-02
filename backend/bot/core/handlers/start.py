import asyncio
import traceback

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from sqlalchemy.ext.asyncio import AsyncSession

from core.services.database import get_user
from core.utils.keyboards import ready_keyboard
from core.utils.messages import BotText
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from core.settings.config import TOKEN

from core.handlers.logger import TgLogger

from shared.database.models import User, TgChannel, UsersToTgChannels

tg_log = TgLogger()
bot: Bot = Bot(TOKEN)


async def start_handler(message: Message, command: CommandObject, user: User, session: AsyncSession):
    """
    Команда /start
    """

    # Извлекаем данные переданные в команду
    deeplink = command.args

    if isinstance(deeplink, str) and deeplink.startswith('invite'):
        role_name = {
            'editor': 'Редактором',
            'moderator': 'Модератором'
        }

        channel_id, role = deeplink.replace('invite', '').split('_')

        if role not in ['editor', 'moderator']:
            await message.answer(text=BotText.error.format(
                reason="Некорректная пригласительная ссылка - недопустимая роль"),
                parse_mode="HTML"
            )
            return

        try:
            query = select(TgChannel).where(TgChannel.id == int(channel_id))
        except ValueError:
            await message.answer(text=BotText.error.format(reason="Некорректная пригласительная ссылка"),
                                 parse_mode="HTML")
            return

        channel = await session.execute(query)
        channel = channel.scalar()

        if not channel:
            await message.answer(text=BotText.error.format(
                reason="Некорректная пригласительная ссылка - канал не найден"), parse_mode="HTML"
            )
            return

        query = insert(UsersToTgChannels).values(
            user_id=message.from_user.id,
            channel_id=channel.id,
            role=role
        ).returning(UsersToTgChannels.user_id)

        await session.execute(query)

        try:
            await session.commit()
        except IntegrityError:
            print(traceback.format_exc())
            await session.rollback()
            await message.answer(text=BotText.error.format(reason="Ошибка при сохранение связи"), parse_mode="HTML")
            return

        owner_user: User = await get_user(session, channel.owner_id)

        if not owner_user:
            await message.answer(text=BotText.error.format(reason="Ошибка при получении owner.id"), parse_mode="HTML")
            return

        await message.answer(text=BotText.added_to_channel.format(
            channel_title=channel.title,
            owner_name=owner_user.name,
            role_name=role_name[role]
        ), parse_mode="HTML")

        await tg_log.message(text=f"Создана связь")
        print(f"Создана связь")
        return


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
