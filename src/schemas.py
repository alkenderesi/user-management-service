"""
Pydantic models.

https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    email: str
    last_login: Optional[datetime]

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserCredentials(BaseModel):
    email: str
    password: str
