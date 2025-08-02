from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.api.core.container import Container
from src.api.schemas.users.add_user_model import AddUserModel
from src.api.schemas.users.read_user_model import ReadUserModel
from uuid import UUID

from src.api.services.users_service import UsersService

router = APIRouter()

@router.get("/user/{user_id}")
@inject
async def read_item(
    user_id: UUID,
    users_service: UsersService = Depends(Provide[Container.users_service]),
):
    model = ReadUserModel(id=user_id)
    return users_service.get_user(model)

@router.post("/users/user_id")
@inject
async def add_item(
    user_id: UUID,
    users_service: UsersService = Depends(Provide[Container.users_service]),
):
    model = AddUserModel(id=user_id)
    return users_service.add_user(model)