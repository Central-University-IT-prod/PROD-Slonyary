import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base
from app.models.images import Image

if TYPE_CHECKING:
    from app.models.images import Image
    from app.models.tg_channels import TgChannel
    from app.models.users import User
    from app.models.vk_channels import VkChannel


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    title: Mapped[str] = mapped_column(String, nullable=False)
    html_text: Mapped[str] = mapped_column(String, nullable=False)
    plain_text: Mapped[str] = mapped_column(String, nullable=False)
    publish_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)

    added_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.now,
    )

    status: Mapped[str] = mapped_column(String, nullable=False, default="draft")  # !!

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="created_posts",
        uselist=False,
        lazy="joined",
    )
    tg_channels: Mapped[list["TgChannel"]] = relationship(
        "TgChannel",
        back_populates="posts",
        uselist=True,
        lazy="selectin",
    )
    vk_channels: Mapped[list["VkChannel"]] = relationship(
        "VkChannel",
        back_populates="posts",
        uselist=True,
        lazy="selectin",
    )
    images: Mapped[list["Image"]] = relationship(
        "Image",
        back_populates="post",
        uselist=True,
        lazy="selectin",
    )
