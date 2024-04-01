import base64
from typing import cast

from aiogram import Bot
from aiogram.types import BufferedInputFile, InputMediaPhoto

from shared.database.models import Image, Post, TgChannel


async def publish_tg_post(post: Post, bot: Bot) -> None:
    media_group = await images_to_file_id_media(post, bot)
    set_caption_to_media_group(post.html_text, media_group)

    for channel in cast(list[TgChannel], post.tg_channels):
        await bot.send_media_group(chat_id=channel.id, media=media_group)


async def images_to_file_id_media(post: Post, bot: Bot) -> list[InputMediaPhoto]:
    images = [image_to_media_photo(image) for image in post.images]
    bot_messages = await bot.send_media_group(chat_id=post.owner_id, media=images)
    return [InputMediaPhoto(media=msg.photo[-1].file_id) for msg in bot_messages]


def image_to_media_photo(image: Image) -> InputMediaPhoto:
    img_data = image.base64.encode()
    content = base64.b64decode(img_data)
    media = BufferedInputFile(file=content, filename="filename")
    return InputMediaPhoto(media=media)


def set_caption_to_media_group(
    caption: str,
    media_group: list[InputMediaPhoto],
) -> None:
    media_group[0].caption = caption
