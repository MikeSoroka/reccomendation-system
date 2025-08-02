# main.py
from fastapi import FastAPI
from src.api.controllers import recommendations_controller
from src.api.controllers import users_controller
from src.api.controllers import movies_controller
from src.api.controllers import interactions_controller
from src.api.core.container import Container

app = FastAPI()

container = Container()
container.wire(modules=container.wiring_config.modules)
app.container = container

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

app.include_router(recommendations_controller.router, tags=["recommendations"])
app.include_router(users_controller.router, tags=["users"])
app.include_router(movies_controller.router, tags=["movies"])
app.include_router(interactions_controller.router, tags=["interactions"])