from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models
from . import schemas
from ..gpt import validate_tag


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(login=user.login, email=user.email, phone_number=user.phone_number,
                          hashed_password=user.password, name=user.name, surname=user.surname,
                          description=user.description, dormitory=user.dormitory,
                          random_coffee_active=user.random_coffee_active,
                          random_coffee_days_delta=user.random_coffee_days_delta)

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
    user = get_user(db, schemas.GetUserFromDB(**dict(data)))
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


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**dict(tag))
    try:
        db.add(db_tag)
        db.commit()
        db.refresh(db_tag)
        return '200'
    except Exception as e:
        raise HTTPException(status_code=500, detail='error while adding tag to DB')


def get_tag(db: Session, tag: str):
    return db.query(models.Tag).filter(models.Tag.tag == tag).first()
