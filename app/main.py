from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from services.crud import get_shortened_urls
from services.schemas import ShortenedUrl
from application import app, get_db  # noqa


@app.get("/api/urls", response_model=List[ShortenedUrl])
def read_urls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    urls = get_shortened_urls(db, skip=skip, limit=limit)
    return urls


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8888,
                log_level="info", reload=True)
