"""User SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True, unique=True)
    name = Column(String)
    telegram_id = Column(BigInteger, unique=True)
    registered_at = Column(DateTime, default=datetime.datetime.now)

    tg_channels = relationship("UserTgChannel", back_populates="user")
    owned_tg_channels = relationship("TgChannel", back_populates="owner")
    created_tg_posts = relationship("TgChannelPost", back_populates="owner")

    vk_channels = relationship("UserVkChannel", back_populates="user")
    owned_vk_channels = relationship("VkChannel", back_populates="owner")
    created_vk_posts = relationship("VkChannelPost", back_populates="owner")
