# main.py
from fastapi import FastAPI
from controllers import reccomendations_controller
from controllers import users_controller
from controllers import movies_controller
from controllers import interactions_controller
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

app.include_router(reccomendations_controller.router, tags=["recommendations"])
app.include_router(users_controller.router, tags=["users"])
app.include_router(movies_controller.router, tags=["movies"])
app.include_router(interactions_controller.router, tags=["interactions"])