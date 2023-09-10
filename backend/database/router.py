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


@router.post("/create_user", response_model=schemas.UserFrontend)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = get_password_hash(user.password)
    return CRUD.create_user(db, user)


@router.post("/get_user", response_model=schemas.User)
def get_user(data: schemas.AuthUser, db: Session = Depends(get_db)):
    user = CRUD.get_user(db, data)
    if compare_password(data.password, user.hashed_password):
        return user
    else:
        raise HTTPException(status_code=403, detail="wrong password")


@router.post("/get_user_for_tg")
def get_user_for_tg(data: schemas.GetUserForTg, db: Session = Depends(get_db)):
    if data.telegram:
        return CRUD.get_user(db, schemas.GetUserFromDB(telegram=data.telegram)).login
    elif data.login:
        return CRUD.get_user(db, schemas.GetUserFromDB(login=data.login)).telegram


@router.put("/add_user_tg")
def add_user_tg(data: schemas.AddUserRandomCoffeeConfig, db: Session = Depends(get_db)):
    return CRUD.add_user_telegram(db, data=data)


@router.get("/get_all_tags")
def get_all_tags(db: Session = Depends(get_db)):
    return CRUD.get_all_tags(db)


@router.get('/get_all_users')
def get_all_users(db: Session = Depends(get_db)):
    return CRUD.get_all_users(db)
