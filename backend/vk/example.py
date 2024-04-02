import asyncio
from pathlib import Path

import httpx

from vk.entities.get_wall_upload_server import (
    GetWallUploadServerInput,
    GetWallUploadServerOutput,
)
from vk.entities.media import Media
from vk.entities.photo import Photo
from vk.entities.save_wall_photo import SaveWallPhotoInput
from vk.entities.upload import UploadPhotoInput, UploadPhotoOutput
from vk.methods.create_post import VkCreatePost
from vk.entities.create_post import CreatePostInput, CreatePostOutput
from vk.methods.get_wall_upload_server import GetWallUploadServer
from vk.methods.save_wall_photo import SaveWallPhoto
from vk.methods.upload import UploadPhoto


GROUP_ID = 123123
KEY = "key"


async def get_wall_upload_server(client, key) -> GetWallUploadServerOutput:
    get_wall_server = GetWallUploadServer(client, key)
    params = GetWallUploadServerInput(group_id=GROUP_ID)
    result = await get_wall_server(params)
    return result.response


async def upload_photo(
    client,
    key,
    upload_server: GetWallUploadServerOutput,
) -> UploadPhotoOutput:
    upload_photo_method = UploadPhoto(client, key)
    filepath = str(Path(__file__).parent.resolve() / "example.jpg")
    params = UploadPhotoInput(
        upload_url=upload_server.upload_url,
        filepath=filepath,
    )
    result = await upload_photo_method(params)
    return result.response


async def save_photo(client, key, photo: UploadPhotoOutput) -> list[Photo]:
    save_wall_photo = SaveWallPhoto(client, key)
    params = SaveWallPhotoInput(
        group_id=GROUP_ID,
        photo=photo.photo,
        server=photo.server,
        hash=photo.hash,
    )
    result = await save_wall_photo(params)
    return result.response


async def create_post(
    client,
    key,
    photos: list[Photo] | None = None,
) -> CreatePostOutput:
    post_create = VkCreatePost(client, key)

    attachments = ",".join(
        (
            str(Media(type="photo", owner_id=photo.owner_id, media_id=photo.id))
            for photo in photos
        )
    ) if photos else None

    params = CreatePostInput(
        owner_id=-GROUP_ID,
        from_group=1,
        message="message",
        attachments=attachments,
        mark_as_ads=0,
        close_comments=0,
        mute_notifications=0,
        copyright=None,
    )
    result = await post_create(params)
    return result.response


async def main() -> None:
    async with httpx.AsyncClient() as client:
        server = await get_wall_upload_server(client, KEY)
        print(server)

        photo = await upload_photo(client, KEY, server)
        print(photo)

        saved_photos = await save_photo(client, KEY, photo)
        print(saved_photos)

        post = await create_post(client, KEY, saved_photos)
        print(post)


if __name__ == "__main__":
    asyncio.run(main())
