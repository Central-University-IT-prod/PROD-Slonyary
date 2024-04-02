from datetime import datetime, timedelta
from typing import cast

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from shared.core.enums import PostStatus
from shared.database.models import Post


async def get_posts_to_publish(db: AsyncSession) -> list[Post]:
    moscow_time_now = datetime.utcnow() + timedelta(hours=2)
    query = sa.select(Post).where(
        Post.status == PostStatus.pending,
        Post.publish_time <= moscow_time_now,
    )
    return cast(list[Post], list(await db.scalars(query)))
