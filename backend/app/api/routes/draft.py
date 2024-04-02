from typing import Annotated

from aiogram.types import BufferedInputFile, InputMediaPhoto
from fastapi import APIRouter, File, Form, UploadFile
from sulguk import transform_html

from app.api.deps import CurrentUserDep, TgBotDepends
from app.schemas import Result
from shared.utils.publish_tg_post import set_caption_to_media_group

router = APIRouter(prefix="/posts/draft", tags=["preview"])


@router.post("", status_code=200)
async def post_preview_draft(
    bot: TgBotDepends,
    user: CurrentUserDep,
    files: Annotated[list[UploadFile], File(default_factory=list)],
    html_text: str = Form(...),
    plain_text: str = Form(...),
) -> Result:
    """
    Я живу в идеальном мире, где юзер не блочит бота, поэтому никаких проверок нет.
    """

    result = transform_html(html_text)
    if files:
        media_group = [
            InputMediaPhoto(
                media=BufferedInputFile(await file.read(), filename=file.filename)
            )
            for file in files
        ]
        set_caption_to_media_group(result, media_group)
        await bot.send_media_group(chat_id=user.id, media=media_group)
    else:
        await bot.send_message(
            chat_id=user.id,
            text=result.text,
            entities=result.entities,
        )

    return Result(status="ok")
