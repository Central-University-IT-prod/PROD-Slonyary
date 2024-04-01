from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase
from app.schemas import PostCreate, PostRead, PostUpdate
from shared.database.models import Post


class CrudPost(CrudBase[Post, PostCreate, PostRead, PostUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Post)
