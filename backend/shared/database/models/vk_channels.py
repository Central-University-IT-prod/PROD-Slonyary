"""Vkontakte channel SQLAlchemy model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database.models.base import AlchemyBaseModel
from shared.database.models.users_to_vk import UsersToVkChannels

if TYPE_CHECKING:
    from shared.database.models.users import User


class VkChannel(AlchemyBaseModel):
    __tablename__ = "vk_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    title: Mapped[str] = mapped_column(String(64), nullable=False)
    access_token: Mapped[str] = mapped_column(String(512), nullable=False)
    added_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    owner: Mapped["User"] = relationship(
        "User",
        uselist=False,
        foreign_keys=owner_id,
        lazy="joined",
    )
    users: Mapped[list["User"]] = relationship(
        secondary=UsersToVkChannels.__table__,
        lazy="selectin",
    )
