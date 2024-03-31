from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.posts import Post
    from app.models.tg_channels import TgChannel


class PostsToTgChannels(Base):
    __tablename__ = "posts_to_tg_channels"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="cascade"),
        primary_key=True,
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("tg_channels.id", ondelete="cascade"),
        primary_key=True,
    )

    post: Mapped["Post"] = relationship(
        "User",
        uselist=False,
        foreign_keys=post_id,
        lazy="joined",
    )
    channel: Mapped["TgChannel"] = relationship(
        "TgChannel",
        uselist=False,
        foreign_keys=channel_id,
        lazy="joined",
    )
