import uuid

from sqlalchemy import ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.mixins.timestamp_mixin import TimestampMixin

class AddressModel(Base, TimestampMixin):
    __tablename__ = "addresses"
    
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("users.id"), unique=True, nullable=False, index=True)
    province_code: Mapped[str] = mapped_column(nullable=False)
    province_name: Mapped[str] = mapped_column(nullable=False)
    regency_code: Mapped[str] = mapped_column(nullable=False)
    regency_name: Mapped[str] = mapped_column(nullable=False)
    subdistrict_code: Mapped[str] = mapped_column(nullable=False)
    subdistrict_name: Mapped[str] = mapped_column(nullable=False)
    village_code: Mapped[str] = mapped_column(nullable=False)
    village_name: Mapped[str] = mapped_column(nullable=False)
    full_address: Mapped[str] = mapped_column(Text(255), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(5), nullable=True)

    user = relationship(
        "UserModel",
        back_populates="address",
    )
