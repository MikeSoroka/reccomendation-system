from sqlmodel import create_engine
from dotenv import load_dotenv
import os

class BaseReadRequest:
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url, echo=True)

    def __init__(self, request_models: list):
        self.models = request_models

    @classmethod
    def submit(cls, models):
        pass