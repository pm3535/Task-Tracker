from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependency import DBSession, current_user
from app.schemas.user import UserCreate,UserResponse, UserLogin
from app.services.auth_service import login
from app.services.user_service import create_user

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register', response_model=UserResponse)
async def register(user_in: UserCreate, db:DBSession):
    try:
        user = await create_user(db, user_in)
        return user
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='user already exist')


@router.post('/login')
async def login_user(user_in: UserLogin, db:DBSession):
    result = await login(db=db, email=user_in.email, password=user_in.password)

    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='onvalid credentials')
    return result


@router.get('/')
async def me(current_user: current_user):
    return current_user
   
