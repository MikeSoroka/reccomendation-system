# main.py
from fastapi import FastAPI
from controllers import reccomendations_controller
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

app.include_router(reccomendations_controller.router, tags=["recommendations"])