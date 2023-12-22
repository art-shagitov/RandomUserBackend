from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import utils
from models import Base

POSTGRES_USER = utils.EnvironmentVariables.get_env("POSTGRES_USER")
POSTGRES_PASSWORD = utils.EnvironmentVariables.get_env("POSTGRES_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
