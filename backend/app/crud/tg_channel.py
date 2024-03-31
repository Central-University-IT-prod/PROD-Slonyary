from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase
from app.models import TgChannel
from app.schemas import TgChannelCreate, TgChannelRead, TgChannelUpdate


class CrudTgChannel(
    CrudBase[
        TgChannel,
        TgChannelCreate,
        TgChannelRead,
        TgChannelUpdate,
    ]
):
    def __init__(self, session: AsyncSession):
        super().__init__(session, TgChannel)
