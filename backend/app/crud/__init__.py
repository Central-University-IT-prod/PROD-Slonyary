from typing import Annotated

from fastapi import Depends

from ..api.deps import SessionDepends
from .images import CrudImage
from .post import CrudPost
from .tg_channel import CrudTgChannel
from .user import CrudUser
from .vk_channel import CrudVkChannel


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


# !! Переместить в deps?
CrudUserDepends = Annotated[CrudUser, Depends(crud_user)]
CrudImageDepends = Annotated[CrudImage, Depends(crud_image)]
CrudTgChannelDepends = Annotated[CrudTgChannel, Depends(crud_tg_channel)]
CrudVkChannelDepends = Annotated[CrudVkChannel, Depends(crud_vk_channel)]
CrudPostDepends = Annotated[CrudPost, Depends(crud_post)]


__all__ = (
    "CrudUserDepends",
    "CrudImageDepends",
    "CrudTgChannelDepends",
    "CrudVkChannelDepends",
    "CrudPostDepends",
)
