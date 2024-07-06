from fastapi import FastAPI
from .database import engine, init_db
from .models import SQLModel, ToDo
from .crud import todo_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(todo_router)
