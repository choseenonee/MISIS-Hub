from sqlalchemy import Column, ForeignKey, Boolean, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import DATERANGE


from db import Base
from association_tables import association_user_clubs, association_user_dormitory_form, association_events_organizers


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone_number = Column(String, nullable=True)
    hashed_password = Column(String)
    name = Column(String)
    surname = Column(String)
    student_card = Column(Integer, unique=True)
    description = Column(Text)
    dormitory = Column(String, nullable=True)

    dormitory_form_responders = relationship("User", secondary=association_user_dormitory_form, foreign_keys=[association_user_dormitory_form.c.owner_id])
    clubs = relationship("Club", secondary=association_user_clubs, back_populates="members")
    events = relationship("Event", secondary=association_events_organizers, back_populates="user_organizer")


class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)

    members = relationship("User", secondary=association_user_clubs, back_populates="clubs")
    events = relationship("Event", secondary=association_events_organizers, back_populates="club_organizer")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    date = Column(DATERANGE)  # date_start, date_end(nullable=True)

    club_organizer = relationship("Club", secondary=association_events_organizers, back_populates="events")
    user_organizer = relationship("User", secondary=association_events_organizers, back_populates="events")


class DormitoryForm(Base):
    __tablename__ = 'dormitory_forms'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    description = Column(Text, index=True)
