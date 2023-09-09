from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import database.CRUD as CRUD
import database.models as models
import database.schemas as schemas
from database.db import engine, SessionLocal

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
    return CRUD.create_user(db, user)


@router.get("/get_user", response_model=schemas.User)
def get_user(data: schemas.GetUser, db: Session = Depends(get_db)):
    user = CRUD.get_user(db, data)
    if user.hashed_password == hash(data.password):
        return user
    else:
        raise HTTPException(status_code=403, detail="wrong password")


@router.put("/add_user_tg")
def add_user_tg(data: schemas.AddUserTelegram, db: Session = Depends(get_db)):
    return CRUD.add_user_telegram(db, data=data)

