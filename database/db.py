from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:asdfghj@localhost:5433/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




if __name__ == '__main__':
    session = SessionLocal()
    try:
        result = session.execute(text('SELECT 1'))

        # Check the result
        if result.scalar() == 1:
            print("Connection to the database successful!")
        else:
            print("Connection to the database failed!")
    except Exception as e:
        print("Error occurred while connecting to the database:", str(e))
    finally:
        # Close the session
        session.close()
