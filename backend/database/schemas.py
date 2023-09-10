from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


class UserBase(BaseModel):
    login: str
    name: str
    surname: str
    phone_number: str | None = None
    email: str | None = None
    description: str | None = None
    dormitory: str | None = None
    random_coffee_active: bool


class GetUserForTg(BaseModel):
    telegram: str | None = None
    login: str | None = None


class GetUserFromDB(BaseModel):
    login: str | None = None
    email: str | None = None
    phone_number: str | None = None
    telegram: str | None = None


class AuthUser(GetUserFromDB):
    password: str


class AddUserRandomCoffeeConfig(GetUserFromDB):
    telegram: str
    random_coffee_days_delta: int


class UserCreate(UserBase):
    password: str

    tags: List[str] = []


class UpdateUserRC(BaseModel):
    telegram: str
    random_coffee_active: bool
    last_random_coffee_meet: datetime
    random_coffee_days_delta: int


class UserFrontend(UserBase):
    tags: list


class User(UserBase):
    id: int
    telegram: str | None = None
    last_random_coffee_meet: datetime | None = None
    random_coffee_days_delta: int | None = None

    form_responders: List[str] = []
    clubs: List[str] = []
    events: List[str] = []
    tags: List[str] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class UserInDB(User):
    hashed_password: str


class ClubCreate(BaseModel):
    title: str
    description: str | None = None


class Club(ClubCreate):
    id: int

    members: List[User] = []
    events: List['Event'] = []
    tags: List['Tag'] = []

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
    tags: List['Tag'] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class FormBase(BaseModel):
    author_id: int
    description: str


class FormCreate(FormBase):
    tags: List['Tag'] = []


class Form(FormCreate):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class TagCreate(BaseModel):
    tag: str


class Tag(TagCreate):
    id: int

    clubs: List[str] = []
    events: List[str] = []
    users: List[str] = []
    forms: List[str] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


# fixing the circular references problems
User.model_rebuild()
UserFrontend.model_rebuild()
UserCreate.model_rebuild()
Club.model_rebuild()
Event.model_rebuild()
FormCreate.model_rebuild()
