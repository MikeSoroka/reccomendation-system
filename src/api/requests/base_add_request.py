from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class BaseAddRequest():
    def __init__(self, request_models: list):
        load_dotenv()
        DATABASE_URL = os.getenv("DATABASE_URL")
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.models = request_models

    @classmethod
    def submit(cls, models):
        pass