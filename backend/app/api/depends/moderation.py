from typing import Annotated

from fastapi import Depends, HTTPException
from starlette import status

from app.api.depends.universal import get_post_with_access_check
from app.api.deps import CrudPostDepends, CurrentUserDep, SessionDepends
from shared.core.enums import PostStatus
from shared.database.models import Post


async def accept_post_dep(
    post: Annotated[Post, Depends(get_post_with_access_check)],
    session: SessionDepends,
) -> Post:
    post.status = PostStatus.pending
    await session.commit()
    return post


async def delete_post_dep(
    post_id: int,
    user: CurrentUserDep,
    session: SessionDepends,
    post_crud: CrudPostDepends,
) -> Post:
    post = await get_post_with_access_check(post_id, user.id, post_crud)

    await session.delete(post)
    await session.commit()

    return post


async def downgrade_post_dep(
    post_id: int,
    user: CurrentUserDep,
    session: SessionDepends,
    post_crud: CrudPostDepends,
) -> Post:
    post = await get_post_with_access_check(post_id, user.id, post_crud)

    if post.status == PostStatus.pending:
        post.status = PostStatus.moderation
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    await session.commit()

    return post
