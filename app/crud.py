from sqlalchemy.orm import Session
from models import User
from schemas import RandomUser


def add_database_user(db: Session, user: RandomUser):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_database_users(db: Session, skip: int, limit: int):
    return db.query(User).offset(skip).limit(limit).all()
