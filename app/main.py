from fastapi import FastAPI, Depends, HTTPException
import schemas
import utils
import random
from database import SessionLocal
from sqlalchemy.orm import Session
import crud

app = FastAPI()
MIN_N = int(utils.EnvironmentVariables.get_env("MIN_N"))
MAX_N = int(utils.EnvironmentVariables.get_env("MAX_N"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/get_random_users', response_model=schemas.RandomUserJsonOutput)
def random_users(db: Session = Depends(get_db)) -> schemas.RandomUserJsonOutput:
    if MIN_N >= MAX_N:
        raise HTTPException(status_code=400,
                            detail="Upper bound for N must be greater than the lower bound, change your .env file")
    elif MIN_N or MAX_N < 0:
        raise HTTPException(status_code=400, detail="MIN_N, MAX_N must be greater than 0, change your .env file")

    N = random.randint(MIN_N, MAX_N)
    users = []
    generator = utils.FakeUserGenerator()
    for _ in range(N):
        user = generator.generate_random_user()
        crud.add_database_user(db, user)
        users.append(user)

    return schemas.RandomUserJsonOutput(quantity=N, users=users)


@app.get('/get_database_users')
def get_database_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[schemas.RandomUser]:
    return crud.get_database_users(db, skip, limit)
