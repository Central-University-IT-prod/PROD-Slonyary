"""Vkontakte channel SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class VkChannel(Base):
    __tablename__ = "vk_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade")
    )
    added_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    owner = relationship("User", back_populates="owned_vk_channels", uselist=False)
    users = relationship("UserVkChannel", back_populates="vk_channel")
