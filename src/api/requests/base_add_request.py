from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class BaseAddRequest():
    def __init__(self, request_models: list):
        load_dotenv()
        DATABASE_URL = os.getenv("DATABASE_URL")
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.models = request_models

    def submit(self):
        with Session(self.engine) as session:
            try:
                for request in self.models:
                    session.add(self.model)
                    session.commit()
            except Exception as e:
                session.rollback()
                raise