import uuid

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.mixins.timestamp_mixin import TimestampMixin

class UserModel(Base, TimestampMixin):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    profile = relationship(
        "ProfileModel",
        back_populates="user",
        uselist=False,
    )
    
    address = relationship(
        "AddressModel",
        back_populates="user",
        uselist=True,
    )