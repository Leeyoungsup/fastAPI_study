from pydantic import BaseModel
from typing import Union
class Todo(BaseModel):
    id: int
    item: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }
        
class TodoItem(BaseModel):
    item: str
    
    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }
        
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None