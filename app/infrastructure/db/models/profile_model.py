import uuid
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ARRAY, Date, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.base import Base
from app.infrastructure.db.mixins.timestamp_mixin import TimestampMixin
from app.schemas.user.profile_schema import Gender

if TYPE_CHECKING:
    from app.infrastructure.db.models.interest_model import InterestModel
    from app.infrastructure.db.models.profile_interest_model import ProfileInterestModel


class ProfileModel(Base, TimestampMixin):
    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("users.id"), unique=True, nullable=False, index=True
    )
    gender: Mapped[Gender] = mapped_column(String(1), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    hobbies: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    phone_numbers: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)

    user = relationship(
        "UserModel",
        back_populates="profile",
    )

    profile_interests: Mapped[list[ProfileInterestModel]] = relationship(
        "ProfileInterestModel",
        back_populates="profile",
        cascade="all, delete-orphan",
    )

    interests: Mapped[list[InterestModel]] = relationship(
        "InterestModel",
        secondary="profiles_interests",
        back_populates="profiles",
        viewonly=True,
    )
