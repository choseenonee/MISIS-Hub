from sqlalchemy import Column, ForeignKey, Boolean, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship


from .db import Base
from .association_tables import association_user_clubs, association_form_tags, association_user_form, association_events_organizers, association_user_tags, association_event_tags, association_club_tags


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone_number = Column(String, nullable=True)
    telegram = Column(String, nullable=True)
    hashed_password = Column(String)
    name = Column(String)
    surname = Column(String)
    description = Column(Text, nullable=True)
    random_coffee_active = Column(Boolean)
    last_random_coffee_meet = Column(DateTime, nullable=True)
    random_coffee_days_delta = Column(Integer)
    dormitory = Column(String, nullable=True)

    form_responders = relationship("User", secondary=association_user_form, foreign_keys=[association_user_form.c.owner_id])
    clubs = relationship("Club", secondary=association_user_clubs, back_populates="members")
    events = relationship("Event", secondary=association_events_organizers, back_populates="user_organizer")
    tags = relationship("Tag", secondary=association_user_tags, back_populates="users")


class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)

    members = relationship("User", secondary=association_user_clubs, back_populates="clubs")
    events = relationship("Event", secondary=association_events_organizers, back_populates="club_organizer")
    tags = relationship("Tag", secondary=association_club_tags, back_populates="clubs")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    date_start = Column(DateTime)
    date_end = Column(DateTime, nullable=True)

    club_organizer = relationship("Club", secondary=association_events_organizers, back_populates="events")
    user_organizer = relationship("User", secondary=association_events_organizers, back_populates="events")
    tags = relationship("Tag", secondary=association_event_tags, back_populates="events")


class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author_login = Column(String)
    form_type = Column(String)
    description = Column(Text, index=True)

    tags = relationship("Tag", secondary=association_form_tags, back_populates="forms")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, unique=True)

    clubs = relationship("Club", secondary=association_club_tags, back_populates="tags")
    events = relationship("Event", secondary=association_event_tags, back_populates="tags")
    users = relationship("User", secondary=association_user_tags, back_populates="tags")
    forms = relationship("Form", secondary=association_form_tags, back_populates="tags")
