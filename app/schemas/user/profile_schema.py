from datetime import date
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.schemas.interest_schema import InterestResponse


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"


class ProfileBase(BaseModel):
    gender: Gender
    birth_date: date | None
    hobbies: list[str] = Field(default_factory=list, max_length=20)
    interests: list[UUID] = Field(default_factory=list, max_length=50)
    phone_numbers: list[str] = Field(default_factory=list, max_length=5)
    
    @field_validator('hobbies')
    @classmethod
    def validate_hobbies(cls, v: list[str]) -> list[str]:
        for hobby in v:
            if len(hobby) > 100:
                raise ValueError('Each hobby must be at most 100 characters')
        return v
    
    @field_validator('phone_numbers')
    @classmethod
    def validate_phone_numbers(cls, v: list[str]) -> list[str]:
        import re
        phone_pattern = re.compile(r'^\+?[0-9]{10,15}$')
        for phone in v:
            if not phone_pattern.match(phone):
                raise ValueError(f'Invalid phone number format: {phone}')
        return v


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    gender: Gender | None = None
    birth_date: date | None = None
    hobbies: list[str] | None = None
    interests: list[UUID] | None = None
    phone_numbers: list[str] | None = None


class ProfileResponse(ProfileBase):
    id: UUID

    # Override field dari ProfileBase
    interests: list[InterestResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)