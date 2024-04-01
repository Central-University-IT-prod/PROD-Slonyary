from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database.models.base import AlchemyBaseModel

if TYPE_CHECKING:
    from shared.database.models.posts import Post
    from shared.database.models.vk_channels import VkChannel


class PostsToVkChannels(AlchemyBaseModel):
    __tablename__ = "posts_to_vk_channels"

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id", ondelete="cascade"),
        primary_key=True,
    )
    channel_id: Mapped[int] = mapped_column(
        ForeignKey("vk_channels.id", ondelete="cascade"),
        primary_key=True,
    )

    post: Mapped["Post"] = relationship(
        "Post",
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
