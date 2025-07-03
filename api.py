from fastapi import FastAPI, Query, Path
from fastapi import APIRouter
from todo import todo_router
from model import Item
import os
import uvicorn
from typing import Optional, Annotated

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

@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(title="The ID of the item to get"),
        q: Optional[str] = Query(default=None, alias="item-query")):
    
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/")
async def create_item(item: Item):
    return item