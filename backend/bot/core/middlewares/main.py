import logging
import traceback
from typing import Any, Awaitable, Callable, Dict

from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from aiogram import BaseMiddleware
from aiogram.types import Message

from core.handlers.logger import TgLogger
from shared.database.models import User
from shared.database.session import db_session_manager

tg_log = TgLogger()

class Middleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        async with db_session_manager() as session:
            query = select(User).where(User.id == event.from_user.id)
            user = await session.execute(query)
            user = user.scalar()

            if not user:
                user = insert(User).values(
                    id=event.from_user.id,
                    username=event.from_user.username,
                    name=event.from_user.first_name
                ).returning(User)

                user = await session.execute(user)
                try:
                    await session.commit()

                    user = user.scalar()

                    await tg_log.message(text=f"Новый пользователь: {event.from_user.first_name}")
                    print(f"Новый пользователь: {event.from_user.first_name}")
                except IntegrityError:
                    user = None
                    await session.rollback()
                    print(traceback.format_exc())

            data['user'] = user
            data['session'] = session

            return await handler(event, data)
