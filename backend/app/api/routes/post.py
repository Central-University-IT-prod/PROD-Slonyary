from fastapi import APIRouter, HTTPException

from app.api.deps import (
    CrudImageDepends,
    CrudPostDepends,
    CrudTgChannelDepends,
    CrudUsersToTgChannelsDepends,
    CrudUsersToVkChannelsDepends,
    CrudVkChannelDepends,
    CurrentUserDep,
    SessionDepends,
)
from app.schemas import (
    PostCreate,
    PostIn,
    PostsToTgChannelsCreate,
    PostsToVkChannelsCreate,
    PostUpdate,
    PreviewPost,
)

router = APIRouter()


@router.get("/", status_code=200)
async def get_posts(user: CurrentUserDep, db: SessionDepends, crud_post: CrudPostDepends) -> list[PreviewPost]:
    posts = crud_post.get_user_posts(user)
    result = []

    for post in posts:
        channel_avatars = []
        for tg_channel in post.tg_channels:
            channel_avatars.append(tg_channel.photo_url)

        result.append(PreviewPost(
            id=post.id,
            status=post.status,
            channel_avatars=channel_avatars,
            publish_time=post.publish_time,
            owner_name=post.owner.name,
            html_text=post.html_text,
            plain_text=post.plain_text,
            is_owner=post.owner.id == user.id,
            photos=post.images,
        ))
    
    return result


@router.post("/", status_code=200)
async def create_post(
    user: CurrentUserDep,
    post_in: PostIn,
    crud_post: CrudPostDepends,
    crud_tg_channel: CrudTgChannelDepends,
    crud_vk_channel: CrudVkChannelDepends,
    crud_users_to_tg_channels: CrudUsersToTgChannelsDepends,
    crud_users_to_vk_channels: CrudUsersToVkChannelsDepends,
    crud_image: CrudImageDepends,
):
    """Create post with status moderation."""

    post_create = PostCreate(
        html_text=post_in.html_text,
        plain_text=post_in.plain_text,
        publish_time=post_in.publish_time,
        owner_id=user.id,
        status="moderation",
    )
    post = await crud_post.create(post_create)

    bulk_tg_posts: list[PostsToTgChannelsCreate] = []
    bulk_vk_posts: list[PostsToVkChannelsCreate] = []

    for channel in post_in.channels:
        if channel.type == "tg":

            tg_channel = crud_tg_channel.get(channel.id)
            if not tg_channel:
                await crud_post.delete(post.id)
                raise HTTPException(404, detail="Канал не найден")

            if not tg_channel in user.tg_channels:
                await crud_post.delete(post.id)
                return HTTPException(403, detail="Нет доступа")

            bulk_tg_posts.append(
                PostsToTgChannelsCreate(post_id=post.id, channel_id=channel.id)
            )

        elif channel.type == "vk":
            vk_channel = crud_vk_channel.get(channel.id)

            if not vk_channel:
                await crud_post.delete(post.id)
                raise HTTPException(404, detail="Канал не найден")

            if not vk_channel in user.vk_channels:
                await crud_post.delete(post.id)
                return HTTPException(403, detail="Нет доступа")

            bulk_vk_posts.append(
                PostsToVkChannelsCreate(psot_id=post.id, channel_id=channel.id)
            )

    tg_posts = await crud_users_to_tg_channels.create_many(bulk_tg_posts)
    vk_posts = await crud_users_to_vk_channels.create_many(bulk_vk_posts)
    images = await crud_image.create_many(post_in.images)

    return {"status": "ok"}


@router.get("/{id}", status_code=200)
async def get_post(
    crud_post: CrudPostDepends, user: CurrentUserDep, id: int
) -> PreviewPost:
    """Получение preview поста."""
    post = await crud_post.get(id)

    if not post:
        raise HTTPException(404, "Не найдено")

    if not await crud_post.is_user_access(user, post) and not post.owner_id == user.id:
        raise HTTPException(403, "Нет доступа")

    channel_avatars = []
    for tg_channel in post.tg_channels:
        channel_avatars.append(tg_channel.photo_url)

    return PreviewPost(
        id=post.id,
        status=post.status,
        channel_avatars=channel_avatars,
        publish_time=post.publish_time,
        owner_name=post.owner.name,
        html_text=post.html_text,
        plain_text=post.plain_text,
        is_owner=post.owner.id == user.id,
        photos=post.images,
    )


@router.delete("/{id}", status_code=202)
async def delete_post(crud_post: CrudPostDepends, user: CurrentUserDep, id: int):
    """Delete post by id."""
    post = await crud_post.get(id)

    if not post:
        return {"status": "ok"}

    if not post.owner_id == user.id:
        return HTTPException(403, "Нет доступа")

    await crud_post.delete(id)
    return {"status": "ok"}


@router.patch("/{id}", status_code=200)
async def update_post(
    crud_post: CrudPostDepends, user: CurrentUserDep, id: int, post_update: PostUpdate
):
    """Updating post."""
    post = await crud_post.get(id)

    if not post:
        return HTTPException(404, "Не найдено")

    if not crud_post.is_user_access(user, post):
        return HTTPException(403, "Нет доступа")

    await crud_post.update(post, post_update)
    return {"status": "ok"}
