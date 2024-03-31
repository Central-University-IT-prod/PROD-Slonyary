from datetime import datetime

from pydantic import BaseModel, Field


class UserTelegramData(BaseModel):
    id: int
    username: str | None = None
    auth_date: datetime
    first_name: str


class UserCreate(BaseModel):
    telegram_id: int
    username: str | None = None
    name: str


class UserUpdate(BaseModel):
    pass


class UserOut(BaseModel):
    id: int
    telegram_id: int
    username: str | None = None
    name: str
