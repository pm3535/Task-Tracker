from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

async def create_user(db:AsyncSession, user_in: UserCreate) -> User:
    result = await db.execute(select(User).where(User.email == user_in.email))
    if result.scalar_one_or_none():
        raise ValueError('user already exsist')
    user = User(email= user_in.email, hashed_password= hash_password(user_in.password))

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_id(db:AsyncSession, user_id:int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_user_by_email(db:AsyncSession, email:str) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


