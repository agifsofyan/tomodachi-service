from dataclasses import dataclass, field
from datetime import date
from uuid import UUID
from app.domain.entities.interest_entity import InterestEntity
from app.schemas.user.profile_schema import Gender

@dataclass
class ProfileEntity:
    id: UUID
    user_id: UUID
    gender: Gender
    birth_date: date | None
    hobbies: list[str]
    phone_numbers: list[str]
    interests: list[InterestEntity] = field(default_factory=list)