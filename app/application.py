from fastapi import FastAPI
from sqlalchemy.exc import DBAPIError

from __about__ import __version__
from routers import heartbeat, versions
from services.db import SessionLocal
from settings.globals import API_PREFIX

APP_NAME = "tinykec"
APP_VERSION = __version__
DEBUG = True
ROUTERS = (heartbeat.router, versions.router)


def get_app() -> FastAPI:
    app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=DEBUG)

    for router in ROUTERS:
        app.include_router(router, prefix=API_PREFIX)

    return app


def get_db():
    session = SessionLocal()
    try:
        yield session
    except DBAPIError:
        session.rollback()
    finally:
        session.close()


app = get_app()
