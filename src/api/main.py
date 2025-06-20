# main.py
from fastapi import FastAPI

# This is where 'app' is defined and becomes the FastAPI application instance
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}