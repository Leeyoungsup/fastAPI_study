from fastapi import FastAPI
from fastapi import APIRouter
from todo import todo_router
from model import Item
import os
import uvicorn

app = FastAPI()
router = APIRouter()
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }
    
@router.get('/hello')
async def say_hello() -> dict:
    return {"message": "Hello!"}

@router.get('/bye')
async def say_bye() -> dict:
    return {"message": "bye!"}
app.include_router(router=router)
app.include_router(todo_router)

host = os.getenv('HOST', '127.0.0.1')
port = int(os.getenv('PORT', '8080'))


@app.post("/items/")
async def create_item(item: Item):
    return item