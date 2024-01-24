from app.auth.auth_schemas import UserCreate
from sqlalchemy.orm import Session
from app.db.models import User
from fastapi.exceptions import HTTPException
from typing import Union, Any
from datetime import datetime, timedelta
from app.config import settings
from jose import jwt

ALGORITHM = "HS256"

async def create_user(user_create: UserCreate, db: Session):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(
                    status_code=404,
                    detail=f"User not found",
                )
    return user


def authenticate(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not user.check_password(password):
        return None
    return user




def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt