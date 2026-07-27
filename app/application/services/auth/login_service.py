from app.core.security import verify_password
from app.schemas.auth_schema import AuthResponse, LoginRequest


class LoginService:
    def __init__(self, repository, token_service):
        self.repository = repository
        self.token_service = token_service

    def execute(self, request: LoginRequest) -> AuthResponse:
        user = self.repository.get_by_email(request.email)

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(request.password, user.password):
            raise ValueError("Invalid email or password")

        token = self.token_service.generate(str(user.id))

        return AuthResponse(access_token=token)
