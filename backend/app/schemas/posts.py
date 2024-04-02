from datetime import datetime

from app.schemas.base import BaseSchema


class Channel(BaseSchema):
    id: int
    type: str


class ChannelRead(BaseSchema):
    id: int
    name: str
    avatar: str
    url: str
    type: str


class PostUpdate(BaseSchema):
    html_text: str | None = None
    plain_text: str | None = None
    publish_time: datetime | None = None


class PostIn(BaseSchema):
    html_text: str | None
    plain_text: str | None
    publish_time: datetime | None = None
    channels: list[Channel] | None = None


class PostCreate(BaseSchema):
    html_text: str | None
    plain_text: str | None
    publish_time: datetime
    owner_id: int
    status: str


class PreviewPost(BaseSchema):
    id: int = 0
    status: str
    channel_avatars: list[str]
    publish_time: datetime | None = None
    owner_name: str
    photos: list[str]
    html_text: str | None = None
    plain_text: str | None = None
    views: int = 0
    reactions: int = 0
    shared: int = 0
    is_owner: bool


class PostRead(PreviewPost):
    owner_avatar: str
    publish_channels: list[ChannelRead]
