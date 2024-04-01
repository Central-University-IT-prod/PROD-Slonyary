import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database.models.base import AlchemyBaseModel
from shared.database.models.users_to_tg import UsersToTgChannels
from shared.database.models.users_to_vk import UsersToVkChannels

if TYPE_CHECKING:
    from shared.database.models.posts import Post
    from shared.database.models.tg_channels import TgChannel
    from shared.database.models.vk_channels import VkChannel


class User(AlchemyBaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    username: Mapped[int] = mapped_column(String(64), nullable=True)
    name: Mapped[str] = mapped_column(String(256), nullable=True)
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
        secondary=UsersToTgChannels.__table__,
        lazy="selectin",
    )
    vk_channels: Mapped[list["VkChannel"]] = relationship(
        secondary=UsersToVkChannels.__table__,
        lazy="selectin",
    )
