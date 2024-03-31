from mypy.typeshed.stdlib.typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.posts import Post
    from app.models.vk_channels import VkChannel


class PostsToVkChannels(Base):
    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="cascade"),
        primary_key=True,
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("vk_channels.id", ondelete="cascade"),
        primary_key=True,
    )

    post: Mapped["Post"] = relationship(
        "User",
        uselist=False,
        foreign_keys=post_id,
        lazy="joined",
    )
    channel: Mapped["VkChannel"] = relationship(
        "VkChannel",
        uselist=False,
        foreign_keys=channel_id,
        lazy="joined",
    )
