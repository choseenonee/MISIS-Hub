from pydantic import BaseModel
from datetime import datetime
from typing import List, Union

from models import *


class UserBase(BaseModel):
    login: str
    name: str
    surname: str
    description: str | None = None
    dormitory: str | None = None


class UserCreate(UserBase):
    password: str
    phone_number: str | None = None
    email: str | None = None


class User(UserBase):
    id: int
    form_responders: List[User] = []
    clubs: List[Club] = []
    events: List[Event] = []
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class ClubCreate(BaseModel):
    title: str
    description: str | None = None


class Club(ClubCreate):
    id: int

    members: List[User] = []
    events: List[Event] = []
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    title: str
    description: str | None = None
    date_start: datetime
    date_end: datetime | None = None


class Event(EventCreate):
    id: int

    club_organizer: Union[Club, None] = None
    user_organizer: Union[User, None] = None
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class FormCreate(BaseModel):
    author_id: int
    description: str


class Form(FormCreate):
    id: int

    tags: List[Tag] = []

    class Config:
        orm_mode = True


class TagCreate(BaseModel):
    tag: str
    is_hard: bool


class Tag(TagCreate):
    id: int

    clubs: List[Club] = []
    events: List[Event] = []
    users: List[User] = []
    forms: List[Form] = []

    class Config:
        orm_mode = True
