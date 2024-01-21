import logging
# from functools import lru_cache
from typing import Any, Optional, Union

from pydantic import AnyUrl, field_validator, ValidationInfo
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Main settings class, defining environment variables."""

    APP_NAME: str = "Fast API Boilerplate"
    DEBUG: bool = False
    LOG_LEVEL: str = "DEBUG"

    EXTRA_CORS_ORIGINS: Optional[Union[str, list[AnyUrl]]]

    @field_validator("EXTRA_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(
        cls,
        val: Union[str, list[str]],
        info: ValidationInfo,
    ) -> Union[list[str], str]:
        """Build and validate CORS origins list.

        By default, the provided frontend URLs are included in the origins list.
        If this variable used, the provided urls are appended to the list.
        """
        default_origins = []

        if val is None:
            return default_origins

        if isinstance(val, str):
            default_origins += [i.strip() for i in val.split(",")]
            return default_origins

        elif isinstance(val, list):
            default_origins += val
            return default_origins

        raise ValueError(f"Not a valid CORS origin list: {val}")

    # Database Credentials
    POSTGRES_DB: Optional[str] = "boilerplate"
    POSTGRES_USER: Optional[str] = "postgres"
    POSTGRES_PASSWORD: Optional[str] = "postgres"
    POSTGRES_HOST: Optional[str] = "postgres"
    POSTGRES_PORT: Optional[str] = "5432"
    DATABASE_URL: Optional[str] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


    class Config:
        """Pydantic settings config."""

        case_sensitive = True
        env_file = ".env"


settings = Settings()