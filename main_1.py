from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
         task: Annotated[STaskAdd, Depends()],
):
    tasks.append(tasks)
    return {"ok": True}

#@app.get("/tasks"
#def get_tasks():
#    task = Task(name="Запиши это видео")
#    return {"data": task}