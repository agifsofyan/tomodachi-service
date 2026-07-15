from uuid import uuid4

from app.core.exceptions.user_exception import UserAlreadyExistsException
from app.domain.entities.user_entity import UserEntity
from app.schemas.auth_schema import RegisterRequest, AuthResponse
from app.core.security import hash_password

class RegisterService:
    
    def __init__(self, repository, token_service):
        self.repository = repository
        self.token_service = token_service

    def execute(self, request: RegisterRequest) -> AuthResponse:
        existing_user = self.repository.get_by_email(request.email)
        if existing_user:
            raise UserAlreadyExistsException()

        hashed_password = hash_password(request.password)
        new_user = UserEntity(
            id=uuid4(),
            name=request.name, 
            email=request.email, 
            password=hashed_password
        )
        
        saved_user = self.repository.save(new_user)
        
        token = self.token_service.generate(str(saved_user.id))

        return AuthResponse(
            access_token=token
        )