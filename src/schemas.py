"""
Pydantic models.

https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models
"""

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    last_login: datetime | None

    class Config:
        from_attributes = True
