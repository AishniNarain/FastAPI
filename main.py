from typing import Union

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel  # type: ignore

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
def home():
    return {"msg":"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/hello/{name}/{age}")
def hello(name:str, age:int):
    return {"name": name,
            "age": age
            }
    
@app.get("/hello")
def hello(name:str, age:int):
    return {"name": name,
            "age": age
            }