from fastapi import APIRouter,HTTPException,status
from app.api.dependency import current_user, DBSession
from app.schemas.task import taskCreate,TaskResponse, TaskUpdate
from app.services.task_service import create_task,get_user_tasks,update_task, delete_task

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post('/', response_model=TaskResponse)
async def create_new_task(
    task_in: taskCreate,
    current_user: current_user,
    db:DBSession
):
    return await create_task(db=db, user_id=current_user.id, task_in=task_in)


@router.get('/', response_model=list[TaskResponse])
async def read_tasks(current_user:current_user, db:DBSession):
    return await get_user_tasks(db, current_user.id)

@router.patch('/{task_id}', response_model=TaskResponse)
async def update_user_task(task_id: int, task_in:TaskUpdate, current_user:current_user, db:DBSession):
    task = await update_task(db=db, task_id=task_id,user_id=current_user.id, task_in=task_in)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    return task

@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_task(task_id:int, current_user:current_user, db:DBSession):
    success = await delete_task(db=db, task_id=task_id, user_id = current_user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')