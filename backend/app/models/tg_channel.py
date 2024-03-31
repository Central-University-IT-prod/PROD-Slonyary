"""Telegram channel SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class TgChannel(Base):
    __tablename__ = "tg_channels"

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    added_at = Column(DateTime, default=datetime.datetime.now)

    owner = relationship("User", back_populates="owned_tg_channels", uselist=False)
    users = relationship("UserTgChannel", back_populates="tg_channel")
    posts = relationship("TgChannelPost", back_populates="tg_channel")
