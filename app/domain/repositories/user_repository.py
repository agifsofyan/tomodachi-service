from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.user_entity import UserEntity

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> UserEntity | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity | None:
        pass