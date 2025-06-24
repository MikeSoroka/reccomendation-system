from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

class BaseAddRequest():
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL, echo=True)

    @classmethod
    def submit(cls, models):
        with Session(cls.engine) as session:
            try:
                for model in models:
                    session.add(model)
                session.commit()
            except Exception as e:
                session.rollback()
                raise