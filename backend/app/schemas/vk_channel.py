from app.schemas.base import BaseSchema


class VkChannelCreate(BaseSchema):
    pass


class VkChannelUpdate(BaseSchema):
    pass


class VkChannelMember(BaseSchema):
    user_id: int
    role: str
    name: str
    photo_url: str | None = None


class VkChannelRead(BaseSchema):
    id: int
    photo_url: str | None = None
    name: str
    username: str | None = None
    description: str | None = None
    subscribers: int
    owner_id: int
    workers: list[VkChannelMember]


class PreviewVkChannel(BaseSchema):
    id: int
    photo_base64: str | None = None
    name: str
    username: str
    subscribers: int = 0
    on_moderation: int = 0
    on_pending: int = 0
    type: str
