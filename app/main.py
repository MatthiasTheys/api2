import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from random import randint
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/{user_id}/heaviestlift", response_model=schemas.Lift)
def read_user_heaviest_lift(user_id: int, db: Session = Depends(get_db)):
    db_lift = crud.get_user_heaviest_lift(db, user_id=user_id)
    if db_lift is None:
        raise HTTPException(status_code=404, detail="User has no lifts")
    return db_lift

@app.get("/users/{user_id}/lifts", response_model=list[schemas.Lift])
def read_user_lifts(user_id: int, db: Session = Depends(get_db)):
    db_lifts = crud.get_user_lifts(db, user_id=user_id)
    if db_lifts is None:
        raise HTTPException(status_code=404, detail="User has no lifts")
    return db_lifts

@app.post("/users/{user_id}/lifts", response_model=schemas.Lift)
def create_user_lift(user_id: int, lift: schemas.LiftCreate, db: Session = Depends(get_db)):
    return crud.create_user_lift(db=db, lift=lift, user_id=user_id)

@app.put("/users/{user_id}/lifts", response_model=schemas.Lift)
def update_user_lift(user_id: int, lift: schemas.LiftCreate, db: Session = Depends(get_db)):
    return crud.update_user_lift(db=db, lift=lift, user_id=user_id)

@app.delete("/users/{user_id}/lifts", response_model=schemas.Lift)
def remove_user_lift(user_id: int, db: Session = Depends(get_db)):
    return crud.remove_user_lift(db=db, user_id=user_id)

@app.delete("/users/{user_id}", response_model=schemas.User)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return crud.remove_user(db=db, user_id=user_id)

    