from typing import Any

from app.api.deps import CurrentUserDep, SessionDep, User
from app.core import security, settings
from app.crud import crud_user
from app.schemas import (
    ChannelOut,
    PostOut,
    PreviewPost,
    PreviewTgChannel,
    TgChannelMember,
    TgChannelOut,
    UserCreate,
    UserOut,
    UserTelegramData,
)
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("/", status_code=200)
async def get_posts(user: CurrentUserDep, db: SessionDep) -> list[PreviewPost]:
    pass


@router.get("/{id}", status_code=200)
async def get_post(user: CurrentUserDep, db: SessionDep, id: int) -> list[TgChannelOut]:
    pass
