from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.interest_entity import InterestEntity

class InterestRepository(ABC):

    @abstractmethod
    def create(self, interest: InterestEntity) -> InterestEntity:
        pass
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> InterestEntity | None:
        pass
    
    @abstractmethod
    def get_by_ids(self, ids: list[UUID]) -> list[InterestEntity]:
        pass
    
    @abstractmethod
    def get_all(self) -> list[InterestEntity]:
        pass

    @abstractmethod
    def update(self, interest: InterestEntity) -> InterestEntity:
        pass
    
    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass