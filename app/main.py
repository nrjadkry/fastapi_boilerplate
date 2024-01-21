import logging
import os
import sys
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.auth import auth_routes

# Logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=(
        "%(asctime)s.%(msecs)03d [%(levelname)s] "
        "%(name)s | %(funcName)s:%(lineno)d | %(message)s"
    ),
    datefmt="%y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


def get_application() -> FastAPI:
    """Get the FastAPI app instance, with settings."""
    _app = FastAPI(
        title=settings.APP_NAME,
        description="Fast api boilerplate",
        debug=settings.DEBUG,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.EXTRA_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(auth_routes.router)

    return _app



app = get_application()


@app.get("/")
def hello():
    return {"hello":"world"}