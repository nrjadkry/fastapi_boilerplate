from fastapi import APIRouter, Depends
from app.db import session
from sqlalchemy.orm import Session
from app.db import session
from app.db.models import User
from app.auth import auth_deps, auth_crud, auth_schemas

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