"""
CRUD requests for user.
"""

from typing import Union

import sqlalchemy
from app.crud.base import CrudBase
from app.models.users import User
from app.schemas import UserCreate, UserUpdate
from sqlalchemy.orm import Session


class CrudUser(CrudBase[User, UserCreate]):
    def __init__(self, Model: type[User]):
        super().__init__(Model)

    async def get_by_telegram_id(
        self, db: Session, telegram_id: int
    ) -> Union[User, None]:
        """
        Getting user from table by email.

        Parameters:
            db: Session - db session to deal with.
            email: str - email of user to get.

        Returns:
            user: User - SQLAlchemy model with user data.
            None - if there isn't such user.
        """
        query = sqlalchemy.select(User).where(User.telegram_id == telegram_id)
        result = await db.scalar(query)
        return result

    async def is_telegram_id(self, db: Session, telegram_id: int) -> bool:
        """
        Checking if there is user with telegram_id.

        Parameters:
            telegram_id: int - telegram id to check
        Returns:
            flag: bool - flag if there is user with given telegram_id.
        """
        query = sqlalchemy.select(User).where(User.telegram_id == telegram_id)
        result = await db.scalar(query)
        return result != None
