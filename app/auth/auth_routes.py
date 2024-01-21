from fastapi import APIRouter, Depends
from app.db import session

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(session.get_db)],
    responses={404: {"description": "Not found"}},
)