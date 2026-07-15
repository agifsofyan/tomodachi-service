import uuid

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.mixins.timestamp_mixin import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.infrastructure.db.models.profile_model import ProfileModel
    from app.infrastructure.db.models.profile_interest_model import ProfileInterestModel

class InterestModel(Base, TimestampMixin):
    __tablename__ = "interests"
    
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    
    profile_interests: Mapped[list["ProfileInterestModel"]] = relationship(
        "ProfileInterestModel",
        back_populates="interest",
        cascade="all, delete-orphan",
    )

    profiles: Mapped[list["ProfileModel"]] = relationship(
        "ProfileModel",
        secondary="profiles_interests",
        back_populates="interests",
        viewonly=True,
    )