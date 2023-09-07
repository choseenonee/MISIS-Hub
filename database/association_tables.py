from sqlalchemy import Table, Column, ForeignKey, Boolean


from db import Base


association_user_clubs = Table(
    "association_user_clubs",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("club_id", ForeignKey("clubs.id"), primary_key=True),
    Column('is_admin', Boolean)
)


association_events_organizers = Table(
    "association_events_organizers",
    Base.metadata,
    Column("event_id", ForeignKey("events.id"), primary_key=True),
    Column("club_organizer", ForeignKey("clubs.id"), primary_key=True, nullable=True),
    Column("user_organizer", ForeignKey("users.id"), primary_key=True, nullable=True),
    Column('is_admin', Boolean)
)


association_user_dormitory_form = Table(
    "association_user_dormitory_form",
    Base.metadata,
    Column("owner_id", ForeignKey("users.id"), primary_key=True),
    Column("dormitory_form_id", ForeignKey("clubs.id"), primary_key=True),
    Column('responded_id', ForeignKey("users.id"))
)