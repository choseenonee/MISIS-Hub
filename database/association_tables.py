from sqlalchemy import Table, Column, ForeignKey, Boolean


from database.db import Base


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
    Column("club_organizer", ForeignKey("clubs.id")),
    Column("user_organizer", ForeignKey("users.id")),
    Column('is_admin', Boolean)
)


association_user_form = Table(
    "association_user_form",
    Base.metadata,
    Column("owner_id", ForeignKey("users.id"), primary_key=True),
    Column("form_id", ForeignKey("forms.id"), primary_key=True),
    Column('responded_id', ForeignKey("users.id"))
)


association_club_tags = Table(
    "association_club_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("club_id", ForeignKey("clubs.id"), primary_key=True, nullable=True),
)


association_user_tags = Table(
    "association_user_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True, nullable=True),
)


association_event_tags = Table(
    "association_event_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("event_id", ForeignKey("events.id"), primary_key=True, nullable=True),
)


association_form_tags = Table(
    "association_form_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("form_id", ForeignKey("forms.id"), primary_key=True, nullable=True),
)