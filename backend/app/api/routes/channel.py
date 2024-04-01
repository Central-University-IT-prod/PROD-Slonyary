from app.api.deps import (
    CrudTgChannelDepends,
    CrudUsersToTgChannelsDepends,
    CurrentUserDep,
)
from app.schemas import PreviewTgChannel, TgChannelMember, TgChannelRead
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
) -> TgChannelRead:
    for tg_channel in await crud_user_to_tg_channel.get_user_tg_channels(user):
        if tg_channel.channel_id == id:
            workers = []
            for tg_user in tg_channel.users:
                workers.append(
                    TgChannelMember(
                        user_id=tg_user.id, role="moderator", name=tg_user.name
                    )
                )
            return TgChannelRead(
                id=tg_channel.id,
                photo_url=tg_channel.photo_url,
                name=tg_channel.name,
                username=tg_channel.username,
                subscribers=0,
                description=tg_channel.description,
                workers=workers,
                type="tg",
            )
    raise HTTPException(404, detail="Not found")
