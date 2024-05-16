from fastapi import FastAPI, Body

app = FastAPI()

from typing import List
from pydantic import BaseModel, Field

class Student(BaseModel):
    id : int
    name: str = Field(None, title="the name of the student", max_length=10)
    age : int
    subjects : List[str] = []

@app.get('/students')
async def display_students():
    data = {
        "id": 1,
        "name": "Aishni Narain",
        "age": 23,
        "subjects": ["English", "Computer Science"]
    }
    s1 = Student(**data)
    return s1

@app.post("/students/")
# async def student_data(s1: Student):
#     return s1

@app.post("/students/")
async def student_data(name:str=Body(...),
marks:int=Body(...)):
    return {"name":name,"marks": marks}

