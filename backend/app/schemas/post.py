from app.schemas.base import BaseSchema


class PostUpdate(BaseSchema):
    pass


class PostCreate(BaseSchema):
    pass


from datetime import datetime

# from app.schemas.user import UserRead
from pydantic import BaseModel


class PreviewPost(BaseModel):
    id: int = 0
    satus: str
    channel_avatars: list[str]
    channel_name: str
    publish_time: datetime
    owner_name: str
    photos: list[str]
    html_text: str | None = None
    plain_text: str | None = None
    views: int = 0
    reactions: int = 0
    shared: int = 0
    is_owner: bool


class ChannelRead(BaseModel):
    id: int
    name: str
    avatar: str
    url: str
    type: str


class PostRead(PreviewPost):
    owner_avatar: str
    publish_channels: list[ChannelRead]
