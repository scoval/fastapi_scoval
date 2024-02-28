from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str | None


@app.get("/tasks")
def get_tasks():
    return "Привет, Серега!!!"
    task = Task(name="Запиши это видео.")
    return {"data": task}