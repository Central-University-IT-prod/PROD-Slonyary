from app.schemas.base import BaseSchema


class TgChannelCreate(BaseSchema):
    pass


class TgChannelUpdate(BaseSchema):
    pass


# from app.schemas.user import UserRead
from pydantic import BaseModel


class TgChannelMember(BaseModel):
    user_id: int
    role: str
    name: str
    photo_url: str | None = None


class TgChannelRead(BaseModel):
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
