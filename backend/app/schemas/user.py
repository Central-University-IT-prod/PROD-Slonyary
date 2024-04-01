from app.schemas.base import BaseSchema


class UserTelegramData(BaseSchema):
    id: int
    username: str | None = None
    auth_date: int
    first_name: str
    hash: str
    photo_url: str | None


class UserCreate(BaseSchema):
    id: int
    username: str | None = None
    name: str


class UserUpdate(BaseSchema):
    pass


class UserRead(BaseSchema):
    id: int
    username: str | None = None
    name: str
