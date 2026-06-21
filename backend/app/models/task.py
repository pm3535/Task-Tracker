from app.db.base import Base 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime, ForeignKey, Enum as SAEnum
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'



class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[TaskStatus]= mapped_column(SAEnum(TaskStatus), default=TaskStatus.TODO, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    owner = relationship('User', back_populates='tasks')


