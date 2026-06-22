from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task, TaskStatus
from app.schemas.task import taskCreate, TaskUpdate


async def create_task(db:AsyncSession, user_id: int, task_in:taskCreate) -> Task:
    task = Task(title= task_in.title, description=task_in.description, user_id=user_id, status=TaskStatus.TODO)
    db.add(task)
    await db.commit()
    await db.refresh(task)

    return task

async def get_user_tasks(db:AsyncSession, user_id:int) -> List[Task]:
    result = await db.execute(select(Task).where(Task.user_id == user_id))
    return result.scalars().all()

async def update_task(db:AsyncSession, task_id:int, task_in: TaskUpdate) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if not task:
        return None
    update_data = task_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db:AsyncSession, task_id:int) -> bool:
    result = await db.execute(select(Task).where(Task.id  == task_id))
    task = result.scalar_one_or_none()
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True

