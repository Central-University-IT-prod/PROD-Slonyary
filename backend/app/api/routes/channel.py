from typing import Any

from app.api.deps import CurrentUserDep, SessionDep, User
from app.core import security, settings
from app.crud import crud_user
from app.schemas import (
    PreviewTgChannel,
    TgChannelMember,
    TgChannelOut,
    UserCreate,
    UserOut,
    UserTelegramData,
)
from fastapi import APIRouter, Depends, HTTPException, status

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
