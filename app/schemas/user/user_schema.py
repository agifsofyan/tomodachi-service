from pydantic import BaseModel, ConfigDict
from app.schemas.user.address_schema import AddressResponse
from app.schemas.user.profile_schema import ProfileResponse


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    
    model_config = ConfigDict(from_attributes=True)
    
class UserWithProfileResponse(BaseModel):
    id: int
    email: str
    name: str
    profile: ProfileResponse | None = None

    model_config = ConfigDict(from_attributes=True)
    
class UserWithProfileAndAddressResponse(BaseModel):
    id: int
    email: str
    name: str
    profile: ProfileResponse | None = None
    address: list[AddressResponse] | None = None

    model_config = ConfigDict(from_attributes=True)