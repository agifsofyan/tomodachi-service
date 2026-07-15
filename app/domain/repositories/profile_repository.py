from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.profile_entity import ProfileEntity

class ProfileRepository(ABC):

    @abstractmethod
    def create(self, profile: ProfileEntity, interest_ids: list[UUID] | None = None) -> ProfileEntity:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> ProfileEntity | None:
        pass

    @abstractmethod
    def update(self, profile: ProfileEntity, interest_ids: list[UUID] | None = None) -> ProfileEntity:
        pass
    
    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass