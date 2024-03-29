"""
App main.

https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
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
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.email and crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.update_user(db, db_user, user)


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_user(db, db_user)


@app.post("/login/")
def login(credentials: schemas.UserCredentials, db: Session = Depends(get_db)):
    if not auth.validate_credentials(db, credentials):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Logged in"}
