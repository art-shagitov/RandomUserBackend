from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import CreateTable
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = "random_users"
    name: Mapped[str] = mapped_column("full_name")
    username: Mapped[str] = mapped_column("login",primary_key=True)
    mail: Mapped[str] = mapped_column("email")
    age: Mapped[int] = mapped_column("age")
    sex : Mapped[str] = mapped_column("gender")
    address : Mapped[str] = mapped_column("address")
    



