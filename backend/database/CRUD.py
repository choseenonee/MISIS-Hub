from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models
from . import schemas
from ..gpt import validate_tag


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(login=user.login, email=user.email, phone_number=user.phone_number,
                          hashed_password=user.password, name=user.name, surname=user.surname,
                          description=user.description, dormitory=user.dormitory,
                          random_coffee_active=user.random_coffee_active)
    db_user.tags = [get_tag(db, tag) for tag in user.tags]
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='error while creating user')
    user_frontend = schemas.UserFrontend(**dict(user))
    return user_frontend


def get_user(db: Session, data: schemas.GetUserFromDB):
    if data.login:
        db_user = db.query(models.User).filter(models.User.login == data.login).first()
    elif data.email:
        db_user = db.query(models.User).filter(models.User.email == data.email).first()
    elif data.phone_number:
        db_user = db.query(models.User).filter(models.User.phone_number == data.phone_number).first()
    elif data.telegram:
        db_user = db.query(models.User).filter(models.User.telegram == data.telegram).first()
    else:
        raise HTTPException(status_code=404, detail='user not found')
    if db_user.tags is not None:
        tag_list = [tag.tag for tag in db_user.tags]
    user = schemas.UserInDB(id=db_user.id, login=db_user.login, name=db_user.name, surname=db_user.surname,
                            phone_number=db_user.phone_number, email=db_user.email, description=db_user.description,
                            dormitory=db_user.dormitory, random_coffee_active=db_user.random_coffee_active,
                            tags=tag_list, telegram=db_user.telegram, clubs=db_user.clubs,
                            last_random_coffee_meet=db_user.last_random_coffee_meet,
                            form_responders=db_user.form_responders, events=db_user.events,
                            hashed_password=db_user.hashed_password, random_coffee_days_delta=db_user.random_coffee_days_delta)
    return user


def get_all_users(db: Session):
    return db.query(models.User).all()


def add_user_telegram(db: Session, data: schemas.AddUserRandomCoffeeConfig):
    user = get_user(db, schemas.GetUserFromDB(**dict(data)))
    user.telegram = data.telegram
    user.random_coffee_days_delta = data.random_coffee_days_delta
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
    for db_tag in db.query(models.Tag).all():
        if db_tag.tag.lower().replace(' ', '') == tag.lower().replace(' ', ''):
            return db_tag
    # return db.query(models.Tag).filter(models.Tag.tag == tag).first()


def get_all_tags(db: Session):
    return db.query(models.Tag).all()
