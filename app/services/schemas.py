from datetime import datetime

from pydantic import BaseModel


class ShortenedUrlBase(BaseModel):
    long: str
    short: str
    # created_at: datetime
    # updated_at: datetime
    # is_active: bool

class ShortenedUrlCreate(ShortenedUrlBase):
    pass

class ShortenedUrl(ShortenedUrlBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True