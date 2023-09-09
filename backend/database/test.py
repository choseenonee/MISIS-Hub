from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import sql

# from CRUD import create_user
# SQLALCHEMY_DATABASE_URL = "postgresql://thechosenone@localhost:5432/postgres" # macOS
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:asdfghj@localhost:5433/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


def drop_all_tables():
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    # Указываем параметры подключения к базе данных
    connection = psycopg2.connect(SQLALCHEMY_DATABASE_URL)

    # Создаем объект-курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    # Получаем список всех таблиц в базе данных
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
    tables = cursor.fetchall()

    # Выполняем DROP и DROP CASCADE для каждой таблицы
    for table in tables:
        table_name = table[0]
        drop_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table_name))
        cursor.execute(drop_query)

    # Подтверждаем изменения в базе данных
    connection.commit()

    # Закрываем соединение с базой данных
    cursor.close()
    connection.close()


def test():
    from models import User, Club, Event, Tag, Base
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    # Создаем объекты пользователей, клубов, событий и тэгов
    user1 = User(name="John", login="john123")
    user2 = User(name="Alice", login="alice456")

    club1 = Club(title="Club A", description="Club A description")
    club2 = Club(title="Club B", description="Club B description")

    event1 = Event(title="Event X", description="Event X description")
    event2 = Event(title="Event Y", description="Event Y description")

    tag1 = Tag(tag="Tag 1", is_hard=True)
    tag2 = Tag(tag="Tag 2", is_hard=False)

    # Добавляем пользователям клубы, события и теги
    user1.clubs.append(club1)
    user1.clubs.append(club2)
    user1.events.append(event1)
    user2.events.append(event2)
    user1.tags.append(tag1)
    user2.tags.append(tag2)

    # Добавляем клубам и событиям теги
    club1.tags.append(tag1)
    club2.tags.append(tag2)
    event1.tags.append(tag1)
    event2.tags.append(tag2)

    # Сохраняем изменения в базе данных
    session.add(user1)
    session.add(user2)
    session.add(club1)
    session.add(club2)
    session.add(event1)
    session.add(event2)
    session.add(tag1)
    session.add(tag2)
    session.commit()

    # Чтение из базы данных для проверки связей
    user = session.query(User).filter_by(name="John").first()
    print(user.clubs)  # Выводит клубы, к которым принадлежит пользователь

    club = session.query(Club).filter_by(title="Club A").first()
    print(club.members)  # Выводит пользователей, принадлежащих к клубу

    event = session.query(Event).filter_by(title="Event X").first()
    print(event.tags)  # Выводит теги, связанные с событием

    tag = session.query(Tag).filter_by(tag="Tag 1").first()
    print(tag.clubs)  # Выводит клубы, связанные с тегом


def test_a_function():
    from models import User, Club, Event, Tag, Form, Base
    from schemas import UserCreate, UserInDB
    from datetime import datetime
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    return create_user(session, UserInDB(**dict(UserCreate(login='aboba', name='zalupa', surname='popa', password='123', random_coffee_active=True, last_random_coffee_meet=datetime.now(), random_coffee_days_delta=5))))


if __name__ == '__main__':
    test()
    # test_a_function()
    # drop_all_tables()
