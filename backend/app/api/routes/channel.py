from fastapi import APIRouter

from app.api.deps import CurrentUserDep, SessionDepends
from app.schemas import PreviewTgChannel, TgChannelRead

router = APIRouter()


@router.get("/tg", status_code=200)
async def get_tg_channels(
    user: CurrentUserDep,
    db: SessionDepends,
) -> list[PreviewTgChannel]:
    pass


@router.get("/tg/{id}")
async def get_tg_channel(
    user: CurrentUserDep,
    db: SessionDepends,
    id: int,
) -> list[TgChannelRead]:
    pass
