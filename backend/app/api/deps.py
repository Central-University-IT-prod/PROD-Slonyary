from typing import Annotated

from app.core import security
from app.crud import (
    CrudImage,
    CrudPost,
    CrudTgChannel,
    CrudUser,
    CrudUsersToTgChannels,
    CrudVkChannel,
)
from fastapi import Depends, Header, HTTPException, status
from jose import JWTError, jwt
from shared.core.config import settings
from shared.database.models import User
from shared.database.session import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession

SessionDepends = Annotated[AsyncSession, Depends(get_db_session)]


def crud_user(db: SessionDepends) -> CrudUser:
    return CrudUser(db)


def crud_image(db: SessionDepends) -> CrudImage:
    return CrudImage(db)


def crud_tg_channel(db: SessionDepends) -> CrudTgChannel:
    return CrudTgChannel(db)


def crud_vk_channel(db: SessionDepends) -> CrudVkChannel:
    return CrudVkChannel(db)


def crud_post(db: SessionDepends) -> CrudPost:
    return CrudPost(db)


def crud_users_to_tg_channels(db: SessionDepends) -> CrudUsersToTgChannels:
    return CrudUsersToTgChannels(db)


CrudImageDepends = Annotated[CrudImage, Depends(crud_image)]
CrudTgChannelDepends = Annotated[CrudTgChannel, Depends(crud_tg_channel)]
CrudVkChannelDepends = Annotated[CrudVkChannel, Depends(crud_vk_channel)]
CrudPostDepends = Annotated[CrudPost, Depends(crud_post)]
CrudUserDepends = Annotated[CrudUser, Depends(crud_user)]
CrudUsersToTgChannelsDepends = Annotated[
    CrudUsersToTgChannels, Depends(crud_users_to_tg_channels)
]


async def get_current_user(
    token: Annotated[str, Header()],
    user_crud: CrudUserDepends,
) -> User:
    try:
        payload = jwt.decode(
            token, "LcH6ouNfUvAhn4AdmjkwkvfzbUHn3ViVHqjt8P1umPc", algorithms=["HS256"]
        )
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(401, detail="Wrong credentials")
    except JWTError:
        raise HTTPException(401, detail="Wrong credentials")
    user = await user_crud.get_by_telegram_id(user_id)
    if user is None:
        raise HTTPException(401, detail="Wrong credentials")
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]


__all__ = (
    "SessionDepends",
    "CrudImageDepends",
    "CrudTgChannelDepends",
    "CrudVkChannelDepends",
    "CrudPostDepends",
    "CrudUserDepends",
    "CurrentUserDep",
)
