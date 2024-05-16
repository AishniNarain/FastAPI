from fastapi import FastAPI, Path, Query
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get('/')
async def home():
    return {"msg":"Hello World!"}

# class SomeDto(BaseModel):
#     data: str = Field(min_length=3, description="Minimum length must be greater than 3",
#                         title="Minimum length must be greater than 3")

# @app.post(path="/")
# async def get_response(request: SomeDto):
#     return "some response"

# @app.exception_handler(RequestValidationError)
# async def handle_error(request: Request, exc: RequestValidationError) -> PlainTextResponse:
#     return PlainTextResponse(str(exc.errors()), status_code=400)

#type hints
@app.get('/hello')
def say_hello(name:str):
    return "Hello "+ name

# class rectangle:
#     def __init__(self, w:int, h:int) ->None:
#         self.width=w
#         self.height=h
        
# def area(r:rectangle)->int:
#     return r.width*r.height
# r1=rectangle(10,20)
# print ("area = ", area(r1))

#path parameters
# @app.get('/home/{name}/{age}')
# def home(name: str, age: int):
#     return {"name": name, "age": age}

#query parameters
# @app.get('/home')
# def home(name: str, age: int):
#     return {"name": name, "age": age}

#path and query parameters
# @app.get('/home/{name}')
# def home(name: str, age: int):
#     return {"name": name, "age": age}

#Path parameters with validations
#query parameters
@app.get('/home/{name}/{age}')
def home(name: str = Path(...,min_length=3,max_length=10),
            age: int = Path(...,ge=10,lt=100)):
    return {"name": name, "age": age}