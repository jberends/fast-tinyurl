from typing import List

from sqlalchemy.orm import Session

from services.models import ShortenedUrl


def get_shortened_url(db: Session, short:str) -> ShortenedUrl:
    return db.query(ShortenedUrl).filter_by(short=short).first()


def get_shortened_urls(db: Session, skip:int = 0, limit=100) -> List[ShortenedUrl]:
    return db.query(ShortenedUrl).offset(skip).limit(limit).all()

