from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.interest_entity import InterestEntity


class ProfileInterestRepository(ABC):

    @abstractmethod
    def add_interests_to_profile(self, profile_id: UUID, interest_ids: list[UUID]) -> None:
        pass

    @abstractmethod
    def remove_interests_from_profile(self, profile_id: UUID, interest_ids: list[UUID]) -> None:
        pass

    @abstractmethod
    def get_profile_interests(self, profile_id: UUID) -> list[InterestEntity]:
        pass

    @abstractmethod
    def clear_profile_interests(self, profile_id: UUID) -> None:
        pass
    
    @abstractmethod
    def replace_profile_interests(self, profile_id: UUID, interest_ids: list[UUID]) -> None:
        pass
