from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task, TaskStatus
from app.schemas.task import taskCreate


async def create_task(db:AsyncSession, user_id: int, task_in:taskCreate) -> Task:
    task = Task(title= task_in.title, description=task_in.description, user_id=user_id, status=TaskStatus.TODO)
    db.add(task)
    await db.commit()
    await db.refresh(task)

    return task

async def get_user_tasks(db:AsyncSession, user_id:int) -> List[Task]:
    result = await db.execute(select(Task).where(Task.user_id == user_id))
    return result.scalars().all()