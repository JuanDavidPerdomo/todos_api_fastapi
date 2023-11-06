from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

# uvicorn cant use de APIRouter Instance, so its necessary to use the fastapi class to deal this task.
app.include_router(todo_router)