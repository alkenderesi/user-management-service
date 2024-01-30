"""User authentication."""

from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas


def validate_credentials(db: Session, credentials: schemas.UserCredentials):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    if not user or user.hashed_password != credentials.password + "notreallyhashed":
        return False

    user.last_login = datetime.now()
    db.commit()

    return True
