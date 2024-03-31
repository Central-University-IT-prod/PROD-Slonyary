import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.posts import Post
    from app.models.tg_channels import TgChannel
    from app.models.vk_channels import VkChannel


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    username: Mapped[int] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String)
    registered_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    created_posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="owner",
        uselist=True,
        lazy="selectin",
    )
    tg_channels: Mapped[list["TgChannel"]] = relationship(
        "TgChannel",
        back_populates="users",
        uselist=True,
        lazy="selectin",
    )
    vk_channels: Mapped[list["VkChannel"]] = relationship(
        "VkChannel",
        back_populates="users",
        uselist=True,
        lazy="selectin",
    )
