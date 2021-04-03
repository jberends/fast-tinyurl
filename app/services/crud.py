from sqlalchemy.orm import Session

from services import models


def get_shortened_url(db: Session, short:str):
    return db.query(models.ShortenedUrls).filter(short=short).first()

def get_shortened_urls(db: Session, skip:int = 0, limit=100):
    return db.query(models.ShortenedUrls).offset(skip).limit(limit).all()

