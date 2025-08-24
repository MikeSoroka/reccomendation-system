from dependency_injector import containers, providers

from src.api.automapper.mapper import Mapper
from src.api.db.repositories.interactions_repository import InteractionsRepository
from src.api.db.repositories.movies_repository import MoviesRepository
from src.api.db.repositories.users_repository import UsersRepository
from src.api.db.session import get_db_session
from src.api.redis.redis_db import RedisDB
from src.api.redis.session import get_redis_async, get_redis_sync, create_sync_pool
from src.api.services.interactions_service import InteractionsService
from src.api.services.movies_service import MoviesService
from src.api.services.users_service import UsersService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules =
            [
                "src.api.controllers.interactions_controller",
                "src.api.controllers.movies_controller",
                "src.api.controllers.users_controller",
                "src.api.redis.repositories.recommender_repository",
                "src.api.controllers.recommendations_controller",
                "src.exporter_service.movielens_export_helper",
                "src.exporter_service.data_export",
                "src.model.train",
            ])

    # Redis
    sync_users_pool = providers.Singleton(create_sync_pool, db=RedisDB.USERS_MAPPING_IDS)
    sync_movies_pool = providers.Singleton(create_sync_pool, db=RedisDB.MOVIES_MAPPING_IDS)
    sync_interactions_pool = providers.Singleton(create_sync_pool, db=RedisDB.INTERACTIONS_MAPPING_IDS)

    db_session = providers.Resource(get_db_session)
    users_mappings_redis_session = providers.Resource(
        get_redis_async,
        db=RedisDB.USERS_MAPPING_IDS
    )
    movies_mappings_redis_session = providers.Resource(
        get_redis_async,
        db=RedisDB.MOVIES_MAPPING_IDS
    )

    interactions_mappings_redis_session = providers.Resource(
        get_redis_async,
        db=RedisDB.INTERACTIONS_MAPPING_IDS
    )

    users_mappings_redis_sync_session = providers.Resource(
        get_redis_sync,
        pool=sync_users_pool
    )
    movies_mappings_redis_sync_session = providers.Resource(
        get_redis_sync,
        pool=sync_movies_pool
    )

    interactions_mappings_redis_sync_session = providers.Resource(
        get_redis_sync,
        pool=sync_interactions_pool
    )

    interactions_repository = providers.Factory(InteractionsRepository, session=db_session)
    movies_repository = providers.Factory(MoviesRepository, session=db_session)
    users_repository = providers.Factory(UsersRepository, session=db_session)

    interactions_service = providers.Singleton(InteractionsService, repository=interactions_repository)
    movies_service = providers.Singleton(MoviesService, repository=movies_repository)
    users_service = providers.Singleton(UsersService, repository=users_repository)

    mapper = providers.Singleton(Mapper)
