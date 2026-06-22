from fastapi import APIRouter, HTTPException, status
from app.api.dependency import DBSession, current_user
from app.services.user_service import get_user_by_id
from app.schemas.user import UserResponse


router = APIRouter(prefix='/users', tags=['/users'])

@router.get('/me', response_model=UserResponse)
async def read_current_user(current_user:current_user):
    return current_user

@router.get('/{user_id}', response_model=UserResponse)
async def read_user(
    user_id:int,
    db:DBSession
):
     user = await get_user_by_id(db, user_id)
     if  not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
     return user
   