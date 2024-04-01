from app.schemas.base import BaseSchema


class ImageCreate(BaseSchema):
    post_id: int
    base64: str


class ImageUpdate(BaseSchema):
    pass


class ImageRead(BaseSchema):
    pass
