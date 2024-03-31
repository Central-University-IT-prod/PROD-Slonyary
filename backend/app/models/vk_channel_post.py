"""Vk channel post SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


class VkChannelPost(Base):
    __tablename__ = "vk_channel_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade")
    )
    vk_channel_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("vk_channels.id", ondelete="cascade")
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    plain_text: Mapped[str] = mapped_column(String, nullable=False)
    publish_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade")
    )
    added_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    owner = relationship("User", back_populates="created_vk_posts", uselist=False)
    vk_channel = relationship(
        "VkChannel", ForeignKey("vk_channels.id", ondelete="cascade"), uselist=False
    )
