from fastapi import APIRouter
from pydantic import BaseModel

from settings.globals import APP_VERSION

router = APIRouter()


class VersionResult(BaseModel):
    """ Version response model. """

    version: str
    # major: int
    # minor: int
    # path: str


@router.get("/version", response_model=VersionResult, name="version")
def get_version() -> VersionResult:
    """ Semantic Version of the application."""
    return VersionResult(version=APP_VERSION)