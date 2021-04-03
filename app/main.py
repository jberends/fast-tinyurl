from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from services.crud import get_shortened_urls, get_shortened_url
from application import app, get_db  # noqa
from services.schemas import ShortenedUrl


@app.get("/api/v1/urls", response_model=List[ShortenedUrl])
def read_urls(db: Session=Depends(get_db),
              skip: int = 0, limit: int = 100):
    urls: List[ShortenedUrl] = get_shortened_urls(db, skip=skip, limit=limit)
    return urls

@app.get("/{short_link}")
def redirect(short_link:str, db: Session=Depends(get_db)):
    obj: ShortenedUrl = get_shortened_url(db=db, short=short_link)
    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="The link does not exist, could not redirect."
        )
    return RedirectResponse(url=obj.long)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8888,
                log_level="info", reload=True)
