from app.db.base import Base 
from sqlalchemy.orm import Mapped, mapped_column, relationship, Boolean
from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from enum import Enum

class TaskStatus(str,Enum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'



class Task(Base):
    __table__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=False)
    status: Mapped[TaskStatus] 
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)


    tasks = relationship('Task', back_populates='owner', cascade='all, delete-orohan')


