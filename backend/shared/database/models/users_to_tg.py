from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from shared.database.models.base import AlchemyBaseModel


class UsersToTgChannels(AlchemyBaseModel):
    __tablename__ = "users_to_tg_channels"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"), primary_key=True
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("tg_channels.id", ondelete="cascade"), primary_key=True
    )
