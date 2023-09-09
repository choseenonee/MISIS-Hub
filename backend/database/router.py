from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from . import CRUD
from . import models
from . import schemas
from .db import engine, SessionLocal
from ..authorization.hash import get_password_hash, compare_password


router = APIRouter(
    prefix="/database",
    tags=['database'],
)


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = get_password_hash(user.password)
    return CRUD.create_user(db, user)


@router.get("/get_user", response_model=schemas.User)
def get_user(data: schemas.GetUserFromDB, db: Session = Depends(get_db)):
    user = CRUD.get_user(db, data)
    if user.hashed_password == hash(data.password):
        return user
    else:
        raise HTTPException(status_code=403, detail="wrong password")


@router.put("/add_user_tg")
def add_user_tg(data: schemas.AddUserTelegram, db: Session = Depends(get_db)):
    return CRUD.add_user_telegram(db, data=data)

