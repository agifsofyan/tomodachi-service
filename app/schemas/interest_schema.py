from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class InterestBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    code: str = Field(min_length=2, max_length=50)


class InterestCreate(InterestBase):
    pass


class InterestUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    code: str | None = Field(default=None, min_length=2, max_length=50)


class InterestResponse(InterestBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)