from typing import Annotated

from fastapi import APIRouter, Depends

from main import Task
from main_1 import tasks, STaskAdd
from repository import TaskRepository
from schemas import STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(
         task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = Task(name="Запиши это видео")
    return {"tasks": tasks}