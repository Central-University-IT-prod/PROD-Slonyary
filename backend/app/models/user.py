"""User SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[int] = mapped_column(String, nullable=True, unique=True)
    name: Mapped[str] = mapped_column(String)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    registered_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    tg_channels = relationship("UserTgChannel", back_populates="user")
    owned_tg_channels = relationship("TgChannel", back_populates="owner")
    created_tg_posts = relationship("TgChannelPost", back_populates="owner")

    vk_channels = relationship("UserVkChannel", back_populates="user")
    owned_vk_channels = relationship("VkChannel", back_populates="owner")
    created_vk_posts = relationship("VkChannelPost", back_populates="owner")
