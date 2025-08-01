from dependency_injector import containers, providers
from numpy.lib._user_array_impl import container

from src.api.db.repositories.InteractionsRepository import InteractionsRepository
from src.api.db.repositories.MoviesRepository import MoviesRepository
from src.api.db.repositories.UsersRepository import UsersRepository
from src.api.db.session import get_db_session


class Container(containers.DeclarativeContainer):
    wiring_config = container.WiringConfiguration(
        modules =
            [
                "src.api.controllers.interactions_controller",
                "src.api.controllers.movies_controller",
                "src.api.controllers.recommendations_controller",
                "src.api.controllers.interactions_controller",
            ])

    session = providers.Resource(get_db_session)

    interactions_repository = providers.Factory(InteractionsRepository)
    movies_repository = providers.Factory(MoviesRepository)
    users_repository = providers.Factory(UsersRepository)
