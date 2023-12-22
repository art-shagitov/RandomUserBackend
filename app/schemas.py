from pydantic import BaseModel


class RandomUser(BaseModel):
    name: str
    username: str
    mail: str
    age: int
    sex: str
    address: str

    class Config:
        from_attributes = True


class RandomUserJsonOutput(BaseModel):
    quantity: int
    users: list[RandomUser]
