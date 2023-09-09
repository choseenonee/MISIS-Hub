from sqlalchemy.orm import Session
from fastapi import HTTPException

import database.models as models
import database.schemas as schemas


def create_user(db: Session, user: schemas.UserInDB):
    db_user = models.User(**dict(user))

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='error while creating user')

    return db_user


def get_user(db: Session, data: schemas.GetUserFromDB):
    if data.login:
        return db.query(models.User).filter(models.User.login == data.login).first()
    elif data.email:
        return db.query(models.User).filter(models.User.email == data.email).first()
    elif data.phone_number:
        return db.query(models.User).filter(models.User )
    else:
        raise HTTPException(status_code=404, detail='user not found')


def get_all_users(db: Session):
    return db.query(models.User).all()


def add_user_telegram(db: Session, data: schemas.AddUserTelegram):
    user = get_user(db, schemas.GetUser(**dict(data)))
    user.telegram = data.telegram
    try:
        db.commit()
        return '200'
    except Exception as e:
        raise HTTPException(status_code=500, detail='error while commiting db on adding telegram')


def create_form(db: Session, form: schemas.FormCreate):
    form_base = schemas.FormBase(**dict(form))
    db_form = models.Form(**dict(form_base))
    db_form.tags = [[get_tag(tag) for tag in form.tags]]

    try:
        db.add(db_form)
        db.commit()
        db.refresh(db_form)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='error while creating form')

    return db_form


def get_all_forms(db: Session):
    return db.query(models.Form).all()


def get_tag(db: Session, tag: str):
    return db.query(models.Tag).filter(models.Tag.tag == tag).first()
