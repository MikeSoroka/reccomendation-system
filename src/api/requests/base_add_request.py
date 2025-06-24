from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os
from abc import ABC, abstractmethod

class BaseAddRequest(ABC):
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL, echo=True)

    @abstractmethod
    @classmethod
    def submit(cls, models):
        pass