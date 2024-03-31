from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.tg_channels import TgChannel
    from app.models.users import User


class UsersToTgChannels(Base):
    __tablename__ = "users_to_tg_channels"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"), primary_key=True
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("tg_channels.id", ondelete="cascade"), primary_key=True
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="tg_channels",
        uselist=False,
        foreign_keys=user_id,
        lazy="joined",
    )
    channel: Mapped["TgChannel"] = relationship(
        "TgChannel",
        back_populates="users",
        uselist=False,
        foreign_keys=channel_id,
        lazy="joined",
    )
