from fastapi import APIRouter

from app.api.deps import CurrentUserDep, SessionDep
from app.schemas import PreviewTgChannel, TgChannelOut

router = APIRouter()


@router.get("/tg", status_code=200)
async def get_tg_channels(
    user: CurrentUserDep, db: SessionDep
) -> list[PreviewTgChannel]:
    pass


@router.get("/tg/{id}")
async def get_tg_channel(
    user: CurrentUserDep, db: SessionDep, id: int
) -> list[TgChannelOut]:
    pass
