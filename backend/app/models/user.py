from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, Boolean
from sqlalchemy import String
from datetime import datetime



class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True,nullable=False)
    create_at : Mapped[datetime] = mapped_column(datetime, default=datetime.utcnow, nullable=False)

    tasks = relationship('Task', back_populates='owner', cascade='all, delete-orphan')
