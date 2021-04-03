from datetime import datetime

from sqlalchemy import Column, Integer, Unicode, Boolean, DateTime, func

from services.db import Base


class ShortenedUrl(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.utcnow())
    updated_at = Column(DateTime, onupdate=func.utcnow())

    long = Column(Unicode(24*1024))
    short = Column(Unicode(64), index=True)
    is_active = Column(Boolean, unique=True, default=True)
