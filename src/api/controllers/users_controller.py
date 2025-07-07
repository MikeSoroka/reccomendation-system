from fastapi import APIRouter
from src.api.requests.users.read_user_request import ReadUserRequest
from src.api.requests.users.add_users_request import AddUsersRequest
from src.api.models.schemas.users.add_user_model import AddUserModel
from src.api.models.schemas.users.read_user_model import ReadUserModel
from uuid import UUID

router = APIRouter()

@router.get("/user/{user_id}")
async def read_item(user_id: UUID):
    model = ReadUserModel(id=user_id)
    return ReadUserRequest.submit(model)

@router.post("/users/user_id")
async def add_item(user_id: UUID):
    model = AddUserModel(id=user_id)
    return AddUsersRequest.submit([model])