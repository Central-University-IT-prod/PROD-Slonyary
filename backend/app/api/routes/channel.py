from app.api.deps import (
    CrudTgChannelDepends,
    CrudUsersToTgChannelsDepends,
    CurrentUserDep,
)
from app.schemas import PreviewTgChannel, TgChannelRead
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/tg", status_code=200)
async def get_tg_channels(
    user: CurrentUserDep,
    crud_user_to_tg_channel: CrudUsersToTgChannelsDepends,
) -> list[PreviewTgChannel]:
    result = []
    for tg_channel in await crud_user_to_tg_channel.get_user_tg_channels(user):
        result.append(
            PreviewTgChannel(
                id=tg_channel.id,
                photo_url=tg_channel.photo_url,
                name=tg_channel.name,
                username=tg_channel.username,
                subscribers=0,
                type="tg",
            )
        )
    return result


@router.get("/tg/{id}")
async def get_tg_channel(
    id: int,
    user: CurrentUserDep,
    crud_tg_channel: CrudTgChannelDepends,
    crud_user_to_tg_channel: CrudUsersToTgChannelsDepends,
) -> list[TgChannelRead]:
    """Pass"""
    pass
