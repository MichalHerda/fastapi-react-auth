from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.auth.models import User


def get_user_by_identifier(db: Session, identifier: str) -> User | None:
    return (
        db.query(User)
        .filter(
            or_(
                User.email == identifier,
                User.username == identifier,
            )
        )
        .first()
    )


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def create_user(
    db: Session,
    password_hash: str,
    email: str | None = None,
    username: str | None = None,
) -> User:
    user = User(
        email=email,
        username=username,
        password_hash=password_hash,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
