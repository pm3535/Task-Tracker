from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus


class taskCreate(BaseModel):
    title:str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

class TaskResponse(BaseModel):
    id:int
    title:str
    description: Optional[str]
    status:TaskStatus
    created_at: datetime
    user_id:int

class Config:
    from_attributes = True