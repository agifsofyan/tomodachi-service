from abc import ABC, abstractmethod
from app.domain.entities.interest_entity import InterestEntity

class InterestRepository(ABC):

    @abstractmethod
    def create(self, interest: InterestEntity) -> InterestEntity:
        pass

    @abstractmethod
    def get_by_profile_id(self, profile_id: int) -> list[InterestEntity]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> InterestEntity | None:
        pass
    
    @abstractmethod
    def get_all(self) -> list[InterestEntity]:
        pass

    @abstractmethod
    def update(self, interest: InterestEntity) -> InterestEntity:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass