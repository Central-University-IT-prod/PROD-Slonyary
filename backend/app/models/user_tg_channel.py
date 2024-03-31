"""User added telegram channels SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class UserTgChannels(Base):
    __tablename__ = "user_tg_channels"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade"), primary_key=True
    )
    tg_channel_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tg_channels.id", ondelete="cascade"), primary_key=True
    )

    user = relationship(
        "User",
        back_populates="tg_channels",
        uselist=False,
        foreign_keys="UserTgChannels.user_id",
    )
    tg_channel = relationship(
        "TgChannel",
        back_populates="users",
        uselist=False,
        foreign_keys="UserTgChannels.tg_channel_id",
    )
