from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import session
from app.auth import auth_schemas
from app.db.models import User


def check_existing_user(user_create: auth_schemas.UserCreate, db: Session = Depends(session.get_db)):
    existing_user = db.query(User).filter(
        User.username == user_create.username or
        User.email == user_create.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists",
        )

    return user_create