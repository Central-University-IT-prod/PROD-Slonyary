from typing import Annotated

from app.api.depends.universal import get_post_with_privileged_access
from app.api.deps import CrudPostDepends, SessionDepends
from fastapi import Depends, HTTPException
from shared.core.enums import PostStatus
from shared.database.models import Post
from starlette import status


async def accept_post_dep(
    post: Annotated[Post, Depends(get_post_with_privileged_access)],
    session: SessionDepends,
) -> Post:
    post.status = PostStatus.pending
    await session.commit()
    return post


async def reject_post_dep(
    post: Annotated[Post, Depends(get_post_with_privileged_access)],
    session: SessionDepends,
    crud_posts: CrudPostDepends,
) -> Post:
    await crud_posts.delete(post.id)
    await session.commit()
    return post


async def downgrade_post_dep(
    session: SessionDepends,
    post: Annotated[Post, Depends(get_post_with_privileged_access)],
) -> Post:
    if post.status != PostStatus.pending:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    post.status = PostStatus.moderation
    await session.commit()

    return post
