from fastapi import HTTPException
from starlette import status

from app.api.deps import CrudPostDepends, CurrentUserDep
from shared.database.models import Post


async def get_post_with_access_check(
    post_id: int,
    user: CurrentUserDep,
    post_crud: CrudPostDepends,
) -> Post:
    post = await post_crud.get(post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not await post_crud.is_privileged_access(user.id, post):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    return post
