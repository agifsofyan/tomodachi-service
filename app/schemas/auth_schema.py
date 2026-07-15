from pydantic import BaseModel, ConfigDict, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "johndoe@example.com",
                "password": "admin123"
            }
        }
    )
    
class RegisterRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "password": "admin123"
            }
        }
    )


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"