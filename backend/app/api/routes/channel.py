from app.api.deps import CurrentUserDep, SessionDepends
from app.crud import CrudTgChannelDepends, CrudUserToTgChannelDepends
from app.schemas import PreviewTgChannel, TgChannelRead
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/tg", status_code=200)
async def get_tg_channels(
    user: CurrentUserDep,
    crud_user_to_tg_channel: CrudUserToTgChannelDepends,
) -> list[PreviewTgChannel]:
    return crud_user_to_tg_channel.get_tg_channels(user)


@router.get("/tg/{id}")
async def get_tg_channel(
    id: int,
    user: CurrentUserDep,
    crud_tg_channel: CrudTgChannelDepends,
    crud_user_to_tg_channel: CrudUserToTgChannelDepends,
) -> list[TgChannelRead]:
    tg_channel = crud_tg_channel.get(id)
    if not tg_channel:
        raise HTTPException(status_code=404, detail="Channel not found")

    if crud_user_to_tg_channel.is_user_access(user, tg_channel):
        return tg_channel
    else:
        raise HTTPException(401, detail="Not enough access")
