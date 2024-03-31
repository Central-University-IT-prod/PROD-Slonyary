"""Telegram channel SQLAlchemy model."""

import datetime

from app.core.db import Base
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TgChannel(Base):
    __tablename__ = "tg_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    owner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade")
    )
    added_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.now
    )

    owner = relationship("User", back_populates="owned_tg_channels", uselist=False)
    users = relationship("UserTgChannel", back_populates="tg_channel")
    posts = relationship("TgChannelPost", back_populates="tg_channel")
