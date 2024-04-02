from http.client import HTTPException
from typing import Annotated, cast

from fastapi import Depends

from app.api.depends.universal import get_post_with_any_access
from app.api.deps import SessionDepends
from app.schemas import ImageIn
from shared.database.models import Image, Post


async def create_image_dep(
    image: ImageIn,
    post: Annotated[Post, Depends(get_post_with_any_access)],
    db: SessionDepends,
) -> Image:
    if len(post.images) >= 10:
        post.images = post.images[:10]
        await db.commit()
        raise HTTPException(409)

    image_db = Image(post_id=post.id, base64=image.base64)
    db.add(image_db)
    await db.commit()
    return image_db


async def get_all_images_dep(
    post: Annotated[Post, Depends(get_post_with_any_access)],
) -> Image:
    return post.images


async def get_image_dep(
    image_id: int,
    post: Annotated[Post, Depends(get_post_with_any_access)],
) -> Image | None:
    for image in cast(list[Image], post.images):
        if image.id == image_id:
            return image
    return None


async def delete_image_dep(
    image_id: int,
    post: Annotated[Post, Depends(get_post_with_any_access)],
    db: SessionDepends,
) -> None:
    for image in cast(list[Image], post.images):
        if image.id == image_id:
            await db.delete(image)
            await db.commit()
            break
