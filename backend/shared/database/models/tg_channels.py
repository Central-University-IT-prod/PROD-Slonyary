"""Telegram channel SQLAlchemy model."""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database.models.base import AlchemyBaseModel
from shared.database.models.posts_to_tg import PostsToTgChannels
from shared.database.models.users_to_tg import UsersToTgChannels

if TYPE_CHECKING:
    from shared.database.models.posts import Post
    from shared.database.models.users import User


class TgChannel(AlchemyBaseModel):
    __tablename__ = "tg_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=True)
    title: Mapped[str] = mapped_column(String(1024), nullable=False)
    photo_url: Mapped[str] = mapped_column(String, nullable=True)
    added_at: Mapped[datetime.datetime] = Column(
        DateTime,
        default=datetime.datetime.now,
    )

    owner: Mapped["User"] = relationship(
        "User",
        foreign_keys=owner_id,
    )
    users: Mapped[list["User"]] = relationship(
        secondary=UsersToTgChannels.__table__,
        lazy="selectin",
    )
    posts: Mapped[list["Post"]] = relationship(
        secondary=PostsToTgChannels.__table__,
        lazy="selectin",
    )
