import uuid

from sqlalchemy import ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.infrastructure.db.base import Base

if TYPE_CHECKING:
    from app.infrastructure.db.models.interest_model import InterestModel
    from app.infrastructure.db.models.profile_model import ProfileModel


class ProfileInterestModel(Base):
    __tablename__ = "profiles_interests"

    profile_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        primary_key=True,
    )

    interest_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("interests.id", ondelete="CASCADE"),
        primary_key=True,
    )

    profile: Mapped[ProfileModel] = relationship(
        "ProfileModel",
        back_populates="profile_interests",
    )

    interest: Mapped[InterestModel] = relationship(
        "InterestModel",
        back_populates="profile_interests",
    )