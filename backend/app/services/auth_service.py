from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.services.user_service import get_user_by_email, get_user_by_id
from app.core.security import verify_password, create_access_token, create_refresh_token, decode_token


async def authenticate_user(db:AsyncSession, email:str, password:str) -> User | None:
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

async def login(db:AsyncSession, email:str, password:str) -> dict | None:
    user = await authenticate_user(db, email, password)

    if not user:
        return None
    access_token = create_access_token({'sub': str(user.id)})
    refresh_token = create_refresh_token({'sub': str(user.id)})

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'token_type': 'bearer'
    }

async def get_user_from_token(db:AsyncSession, token:str) -> User | None:
    payload = decode_token(token)

    if not payload:
        return None
    user_id = payload.get('sub')
    return await get_user_by_id(db, int(user_id))