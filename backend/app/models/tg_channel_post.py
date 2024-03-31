"""Telegram channel post SQLAlchemy model."""

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
from sqlalchemy.orm import relationship


class TgChannelPost(Base):
    __tablename__ = "tg_channel_posts"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    tg_channel_id = Column(Integer, ForeignKey("tg_channels.id", ondelete="cascade"))
    title = Column(String, nullable=False)
    md_text = Column(String, nullable=False)
    publish_time = Column(DateTime)
    is_published = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    added_at = Column(DateTime, default=datetime.datetime.now)

    owner = relationship("User", back_populates="created_posts", uselist=False)
    tg_channel = relationship("TgChannel", back_populates="posts", uselist=False)
