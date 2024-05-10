from fastapi import FastAPI, Request
# from pydantic import BaseModel, Field
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse


app = FastAPI()

@app.get('/')
def home():
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