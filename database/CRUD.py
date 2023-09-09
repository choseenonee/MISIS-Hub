from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas


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


def get_user(db: Session, data: schemas.GetUser):
    if data.login:
        return db.query(models.User).filter(models.User.login == data.login).first()
    elif data.email:
        return db.query(models.User).filter(models.User.email == data.email).first()
    elif data.phone_number:
        return db.query(models.User).filter(models.User )
    else:
        return '404 not found'


def create_form(db: Session, form: schemas.FormCreate):
    form.tags = [get_tag(tag) for tag in form.tags]
    db_form = models.Form(**dict(form))

    try:
        db.add(db_form)
        db.commit()
        db.refresh(db_form)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='error while creating form')

    return db_form


def get_tag(db: Session, tag: str):
    return db.query(models.Tag).filter(models.Tag.tag == tag).first()
