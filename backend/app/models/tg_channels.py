"""Telegram channel SQLAlchemy model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.posts import Post
    from app.models.users import User


class TgChannel(Base):
    __tablename__ = "tg_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    username: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    added_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.now
    )

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="owned_tg_channels",
        foreign_keys=owner_id,
    )
    users: Mapped[list["User"]] = relationship(
        "UserTgChannel",
        back_populates="tg_channels",
        lazy="selectin",
    )
    posts: Mapped[list["Post"]] = relationship(
        "TgChannelPost",
        back_populates="tg_channels",
        lazy="selectin",
    )
