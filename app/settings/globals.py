from pathlib import Path

from starlette.config import Config

from __about__ import __version__

package_root: Path = Path(__file__).parent.parent.parent / ".env"
config: Config = Config(package_root if package_root.exists() else None)

APP_NAME: str = "Latex docker microservice"
APP_VERSION: str = __version__

DATABASE_URL: str = config("DATABASE_URL", cast=str, default="sqlite:///./sql_app.sqlite")
# DATABASE_URL: str = config("DATABASE_URL", cast=str, default="postgresql://user:pass@localhost/tinyurl")

# Application Root. This is the directory where './app' is in.
APP_ROOT: Path = Path(__file__).parents[2]

API_PREFIX: str = config("API_PREFIX", cast=str, default="/api/v1")

# # Very simple Authentication with API KEY
# API_KEY: Optional[Secret] = config("API_KEY", cast=Secret, default=None)
# API_AUTHORIZATION_HEADER: str = config(
#     "API_AUTHORIZATION_HEADER", cast=str, default="Token"
# )

# Set to True to enable debug mode
DEBUG: bool = config("DEBUG", cast=bool, default=True)

print(
    f"""
{APP_ROOT=}
{DEBUG=}
{DATABASE_URL=}
"""
)
