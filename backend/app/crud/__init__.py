from .images import CrudImage
from .post import CrudPost
from .tg_channel import CrudTgChannel
from .user import CrudUser
from .user_to_tg_channel import CrudUsersToTgChannels
from .vk_channel import CrudVkChannel

__all__ = (
    "CrudImage",
    "CrudPost",
    "CrudTgChannel",
    "CrudUser",
    "CrudVkChannel",
    "CrudUsersToTgChannels",
)
