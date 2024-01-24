from fastapi import APIRouter, Depends, HTTPException
from app.db import session
from sqlalchemy.orm import Session
from app.db import session
from app.db.models import User
from app.auth import auth_deps, auth_crud, auth_schemas
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from app.config import settings


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(session.get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("/signup/", response_model=auth_schemas.UserOut)
async def signup(user_create: auth_schemas.UserCreate = Depends(auth_deps.check_existing_user), 
                db: Session = Depends(session.get_db)):

    return await auth_crud.create_user(user_create, db)


@router.post("/login/")
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(session.get_db), 
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = auth_crud.authenticate(
        db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return auth_schemas.Token(
        access_token=auth_crud.create_access_token(
            user.id, access_token_expires
        )
    )