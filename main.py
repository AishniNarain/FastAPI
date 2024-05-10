from typing import Union

from fastapi import FastAPI, Path, Query # type: ignore
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

# #Path parameters
# @app.get("/hello/{name}/{age}")
# def hello(name:str, age:int):
#     return {"name": name,
#             "age": age
#             }

#Query parameters
# @app.get("/hello")
# def hello(name:str, age:int):
#     return {"name": name,
#             "age": age
#             }
    
#Path parameters with validations
@app.get("/hello/{name}/{age}")
def hello(name:str = Path(...,min_length=3,max_length =10), age:int = Path(...,ge=1,le=100)):
    return {"name": name,
            "age": age
            }
    
#Query parameters with validations
@app.get("/hello")
def hello(name:str, age:int,percent:float=Query(..., ge=20, le=100)):
    return {"name": name,
            "age": age
            }
