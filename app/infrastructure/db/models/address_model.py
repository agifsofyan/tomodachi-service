from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.mixins.timestamp_mixin import TimestampMixin

class AddressModel(Base, TimestampMixin):
    __tablename__ = "addresses"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False, index=True)
    province_id: Mapped[int] = mapped_column(nullable=False)
    province_name: Mapped[str] = mapped_column(nullable=False)
    regency_id: Mapped[int] = mapped_column(nullable=False)
    regency_name: Mapped[str] = mapped_column(nullable=False)
    subdistrict_id: Mapped[int] = mapped_column(nullable=False)
    subdistrict_name: Mapped[str] = mapped_column(nullable=False)
    full_address: Mapped[str] = mapped_column(Text(255), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(5), nullable=True)

    user = relationship(
        "UserModel",
        back_populates="address",
    )
