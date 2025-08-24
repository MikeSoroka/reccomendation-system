from typing import AsyncIterator, Iterator

import redis as redis_sync
import redis.asyncio as redis_async
from contextlib import asynccontextmanager, contextmanager

from redis import ConnectionPool
from redis.asyncio.connection import ConnectionPool as AsyncConnectionPool

from src.api.redis.redis_db import RedisDB

def create_sync_pool(db: RedisDB) -> ConnectionPool:
    pool = redis_sync.ConnectionPool(
        host="localhost",
        port=6379,
        db=db.value,
        socket_connect_timeout=30,
        socket_timeout=30,
        max_connections=20,
    )

    return pool


def get_async_pool(db: int) -> AsyncConnectionPool:
    pool = AsyncConnectionPool(
        host="localhost",
        port=6379,
        db=db,
        socket_connect_timeout=30,
        socket_timeout=30,
    )

    return pool

@asynccontextmanager
async def get_redis_async(db: RedisDB) -> AsyncIterator[redis_async.Redis]:
    client = redis_async.Redis(
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

@contextmanager
def get_redis_sync(pool:ConnectionPool) -> Iterator[redis_sync.Redis]:
    client = redis_sync.Redis(
        connection_pool=pool
    )
    try:
        yield client
    finally:
        pass