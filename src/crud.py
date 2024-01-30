"""
Create, Read, Update, and Delete.

https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils
"""

from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        hashed_password=user.password + "notreallyhashed",
        name=user.name,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, db_user: models.User, user: schemas.UserUpdate):
    if user.name:
        db_user.name = user.name

    if user.email:
        db_user.email = user.email

    if user.password:
        db_user.hashed_password = user.password + "notreallyhashed"

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, db_user: schemas.User):
    db.delete(db_user)
    db.commit()

    return db_user
