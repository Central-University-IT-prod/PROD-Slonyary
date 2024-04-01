from app.crud.base import CrudBase
from app.schemas import PostCreate, PostRead, PostUpdate
from shared.database.models import Post
from sqlalchemy.ext.asyncio import AsyncSession


class CrudPost(CrudBase[Post, PostCreate, PostRead, PostUpdate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Post)

    async def create(self, obj_in: PostCreate) -> Post:
        db_obj = Post(
            owner_id=obj_in.owner_id,
            html_text=obj_in.html_text,
            plain_text=obj_in.plain_text,
            publish_time=obj_in.publish_time,
            is_published=False,
            status=obj_in.status,
        )
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj
