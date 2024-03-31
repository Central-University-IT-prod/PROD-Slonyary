"""User vkontakte channels SQLAlchemy model."""

import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class UserVkChannels(Base):
    __tablename__ = "user_vk_channels"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), primary_key=True)
    vk_channel_id = Column(Integer, ForeignKey("vk_channels.id", ondelete="cascade"), primary_key=True)

    user = relationship("User", back_populates="vk_channels", uselist=False, foreign_keys='UserVkChannels.user_id')
    vk_channel = relationship("TgChannel", back_populates="users", uselist=False, foreign_keys="UserVkChannels.vk_channel_id")
    
