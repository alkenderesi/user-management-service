"""
App main.

https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db, user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)

    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_data: dict[str, Any], db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    valid_attributes = {"name", "email", "password"}

    if len(user_data) > len(valid_attributes):
        raise HTTPException(status_code=400, detail="Too many attributes")

    if invalid_attributes := set(user_data) - valid_attributes:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid attributes: {', '.join(invalid_attributes)}",
        )

    if "email" in user_data and crud.get_user_by_email(db, user_data["email"]):
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.update_user(db, db_user, user_data)
