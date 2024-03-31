from datetime import datetime

# from app.schemas.user import UserOut
from pydantic import BaseModel, Field


class TgChannelMember(BaseModel):
    user_id: int
    role: str
    name: str
    photo_url: str | None = None


class TgChannelOut(BaseModel):
    id: int
    photo_url: str | None = None
    name: str
    username: str | None = None
    description: str | None = None
    subscribers: int
    owner_id: int
    workers: list[TgChannelMember]


class PreviewTgChannel(BaseModel):
    id: int
    photo_url: str | None = None
    name: str
    username: str
    subscribers: int
