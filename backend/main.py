from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn

from database.router import router
from database import models, schemas, CRUD
from database.db import engine, SessionLocal
from match_random_coffee import match_users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_matches", tags=['logic'])
def get_matches(db: Session = Depends(get_db)):
    all_users = CRUD.get_all_users(db)
    matched_users = match_users(all_users)
    return matched_users


if __name__ == "__main__":
    uvicorn.run(app)
