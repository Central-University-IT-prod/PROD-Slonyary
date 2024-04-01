from datetime import datetime
from typing import cast

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from shared.core.enums import PostStatus
from shared.database.models import Post


async def get_tg_posts_to_publish(session: AsyncSession) -> list[Post]:
    query = sa.select(Post).where(
        Post.status == PostStatus.pending,
        Post.publish_time <= datetime.utcnow(),
    )
    return cast(list[Post], await session.scalars(query))
