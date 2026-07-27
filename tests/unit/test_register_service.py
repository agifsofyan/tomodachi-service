from uuid import uuid4

import pytest

from app.application.services.auth.register_service import RegisterService
from app.domain.entities.user_entity import UserEntity
from app.schemas.auth_schema import RegisterRequest


class TestRegisterService:
    def test_register_success(self):
        class MockRepository:
            def get_by_email(self, email: str):
                return None

            def save(self, user: UserEntity) -> UserEntity:
                return UserEntity(
                    id=uuid4(), name=user.name, email=user.email, password=user.password
                )

        class MockTokenService:
            def generate(self, user_id: str) -> str:
                return "mock_token_123"

        service = RegisterService(MockRepository(), MockTokenService())
        request = RegisterRequest(
            name="Test User", email="test@example.com", password="password123"
        )

        result = service.execute(request)

        assert result.access_token == "mock_token_123"
        assert result.token_type == "bearer"

    def test_register_user_already_exists(self):
        class MockRepository:
            def get_by_email(self, email: str):
                return UserEntity(
                    id=uuid4(), name="Existing", email=email, password="hash"
                )

        class MockTokenService:
            def generate(self, user_id: str) -> str:
                return "mock_token"

        service = RegisterService(MockRepository(), MockTokenService())
        request = RegisterRequest(
            name="Test User", email="existing@example.com", password="password123"
        )

        with pytest.raises(Exception):
            service.execute(request)
