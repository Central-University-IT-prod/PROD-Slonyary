from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase

from app.models import Post
from app.schemas import PostCreate, PostRead, PostUpdate


class CrudPost(CrudBase[Post, PostCreate, PostRead, PostUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Post)
