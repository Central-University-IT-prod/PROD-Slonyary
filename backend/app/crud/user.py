import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase
from app.schemas import UserCreate, UserRead, UserUpdate
from shared.database.models.users import User


class CrudUser(CrudBase[User, UserCreate, UserRead, UserUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, User)

    async def get_by_telegram_id(
        self,
        telegram_id: int,
    ) -> User | None:
        query = sa.select(User).where(User.telegram_id == telegram_id)
        result = await self.db.scalar(query)
        return result

    async def is_exists(self, telegram_id: int) -> bool:
        return bool(await self.get_by_telegram_id(telegram_id))
