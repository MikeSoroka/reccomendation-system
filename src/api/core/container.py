from dependency_injector import containers, providers

from src.api.db.repositories.interactions_repository import InteractionsRepository
from src.api.db.repositories.movies_repository import MoviesRepository
from src.api.db.repositories.users_repository import UsersRepository
from src.api.db.session import get_db_session
from src.api.redis.session import get_redis_session
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
                "src.api.controllers.recommendations_controller",
                "src.exporter_service.movielens_export_helper",
                "src.exporter_service.data_export",
            ])

    db_session = providers.Resource(get_db_session)
    redos_session = providers.Resource(get_redis_session)

    interactions_repository = providers.Factory(InteractionsRepository, session=db_session)
    movies_repository = providers.Factory(MoviesRepository, session=db_session)
    users_repository = providers.Factory(UsersRepository, session=db_session)

    interactions_service = providers.Singleton(InteractionsService, repository=interactions_repository)
    movies_service = providers.Singleton(MoviesService, repository=movies_repository)
    users_service = providers.Singleton(UsersService, repository=users_repository)
