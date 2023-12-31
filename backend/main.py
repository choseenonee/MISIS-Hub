import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn
from dotenv import load_dotenv

from .database.router import router
from .database import models, schemas, CRUD
from .database.db import engine, SessionLocal
from .match_random_coffee import match_users
from . import gpt

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


dotenv_relative_path = '.env'
dotenv_path = os.path.abspath(dotenv_relative_path)

load_dotenv(dotenv_path)
predefined_tags_raw = os.getenv('PREDEFINED_TAGS').split(' ')

app.include_router(router)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def initialize_tags():
    global predefined_tags_raw

    predefined_tags = []

    for i in range(len(predefined_tags_raw)-1):
        if predefined_tags_raw[i][0].isupper() and predefined_tags_raw[i+1][0].isupper():
            predefined_tags.append(predefined_tags_raw[i])
        elif predefined_tags_raw[i][0].isupper() and predefined_tags_raw[i+1][0].islower():
            predefined_tags.append(predefined_tags_raw[i] + ' ' + predefined_tags_raw[i+1])

    db = SessionLocal()
    if len(CRUD.get_all_tags(db)) == 0:
        for tag_name in predefined_tags:
            tag = models.Tag(tag=tag_name)
            db.add(tag)
        db.commit()
        db.close()


@app.get("/get_matches", tags=['logic'])
def get_matches(db: Session = Depends(get_db)):
    all_users = CRUD.get_all_users(db)
    matched_users = match_users(all_users)
    return matched_users


@app.get("/get_questions", tags=['logic'])
def get_questions():
    questions = gpt.get_questions()
    return questions


@app.post("/create_tag", tags=['logic'])
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    if CRUD.get_tag(db, tag.tag) is None:
        if gpt.validate_tag(tag.tag):
            CRUD.create_tag(db, tag)
            return JSONResponse(status_code=200, content={"message": "Success"})
        else:
            raise HTTPException(status_code=403, detail='tag didnt passed validation')
    else:
        raise HTTPException(status_code=404, detail="tag that you are trying to add already in database")


if __name__ == "__main__":
    uvicorn.run(app)
