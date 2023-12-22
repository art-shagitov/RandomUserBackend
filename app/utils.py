
from faker import Faker
from schemas import RandomUser
import random
import os
from dotenv import load_dotenv
from pathlib import Path

class FakeUserGenerator:
    fake = Faker()
    def generate_random_user(cls):
        profile =  cls.fake.profile(fields=["name", "username", "mail", "sex", "address"]) 
        return RandomUser(**(profile | {"age": random.randint(10,80)}))
    
class EnvironmentVariables:
    config = load_dotenv(dotenv_path = Path("../.env"))
    @staticmethod
    def get_env(key: str):
        return os.getenv(key)