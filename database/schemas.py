from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Union

from database.models import *


class UserBase(BaseModel):
    login: str
    name: str
    surname: str
    description: str | None = None
    dormitory: str | None = None
    random_coffee_active: bool
    random_coffee_days_delta: int


class GetUserFromDB(BaseModel):
    login: str | None = None
    email: str | None = None
    phone_number: str | None = None


class GetUser(GetUserFromDB):
    password: str


class AddUserTelegram(GetUser):
    telegram: str


class UserCreate(UserBase):
    password: str
    phone_number: str | None = None
    email: str | None = None


class UserInDB(UserCreate):
    hashed_password: str = Field(..., alias='password')


class User(UserBase):
    id: int
    telegram: str | None = None
    last_random_coffee_meet: datetime | None = None

    form_responders: List[User] = []
    clubs: List[Club] = []
    events: List[Event] = []
    tags: List[Tag] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class ClubCreate(BaseModel):
    title: str
    description: str | None = None


class Club(ClubCreate):
    id: int

    members: List[User] = []
    events: List[Event] = []
    tags: List[Tag] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


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
        from_attributes = True
        arbitrary_types_allowed = True


class FormBase(BaseModel):
    author_id: int
    description: str


class FormCreate(FormBase):
    tags: List[str] = []


class Form(FormCreate):
    id: int

    tags: List[Tag] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


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
        from_attributes = True
        arbitrary_types_allowed = True
