from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os
from abc import ABC, abstractmethod

class BaseAddRequest():
    def __init__(self, request_models: list):
        load_dotenv()
        DATABASE_URL = os.getenv("DATABASE_URL")
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.models = request_models

    @abstractmethod
    @classmethod
    def submit(cls, models):
        pass