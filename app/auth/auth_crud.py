from app.auth.auth_schemas import UserCreate
from sqlalchemy.orm import Session
from app.db.models import User

async def create_user(user_create: UserCreate, db: Session):
    db_user = User(**user_create.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user