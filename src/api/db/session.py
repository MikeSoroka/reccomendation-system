from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_url = os.getenv("DATABASE_URL")
engine = create_async_engine(database_url, echo=True)

AsyncSession = sessionmaker(
    engine=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

@asynccontextmanager
async def get_db_session():
    session = AsyncSession()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
