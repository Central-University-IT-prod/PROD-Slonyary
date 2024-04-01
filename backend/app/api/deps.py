from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security
from app.crud import (
    CrudImage,
    CrudPost,
    CrudTgChannel,
    CrudUser,
    CrudUsersToTgChannels,
    CrudVkChannel,
)
from shared.database.models import User
from shared.database.session import get_db_session

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
    hash: Annotated[str, Header()],
    data_check_string: Annotated[str, Header()],
    user_crud: CrudUserDepends,
) -> User:
    if security.verify_user_data(data_check_string, hash):
        for row in data_check_string.split("\n"):
            key, value = row.split("=")
            if key == "id":
                return await user_crud.get_by_telegram_id(int(value))
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Данные неверны",
        )


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
