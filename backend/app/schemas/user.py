from datetime import datetime

from app.schemas.base import BaseSchema


class UserTelegramData(BaseSchema):
    id: int
    username: str | None = None
    auth_date: datetime
    first_name: str


class UserCreate(BaseSchema):
    telegram_id: int
    username: str | None = None
    name: str


class UserUpdate(BaseSchema):
    pass


class UserRead(BaseSchema):
    id: int
    telegram_id: int
    username: str | None = None
    name: str
