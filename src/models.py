"""
Database models.

https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models
"""

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    last_login = Column(DateTime(timezone=True), nullable=True)
