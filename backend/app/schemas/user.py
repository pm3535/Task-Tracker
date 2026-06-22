from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    is_active:bool
    created_at:datetime

class UserLogin(BaseModel):
    email:EmailStr
    password:str



class Config:
    from_attributes = True