from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import User
from app.core.security import decode_token
from app.services.user_service import get_user_by_id



DBSession = Annotated[AsyncSession, Depends(get_db)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

async def get_current_user(token:Annotated[str, Depends(oauth2_scheme)], db: DBSession) -> User:
    payload = decode_token(token)

    if not payload:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token')
    user_id = payload.get('sub')
    if not user_id:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token missing user_id')
    user = await get_user_by_id(db, int(user_id))

    if not user:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='user not found')
    
    return user

current_user = Annotated[User, Depends(get_current_user)]
