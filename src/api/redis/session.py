from typing import AsyncIterator

import redis.asyncio as redis
from contextlib import asynccontextmanager

from src.api.redis.redis_db import RedisDB


@asynccontextmanager
async def get_redis_session(db: RedisDB) -> AsyncIterator[redis.Redis]:
    client = redis.Redis(
        host="localhost",
        port=6379,
        db=db.value,
        socket_connect_timeout=30,
        socket_timeout=30,
    )
    try:
        yield client
    finally:
        await client.close()