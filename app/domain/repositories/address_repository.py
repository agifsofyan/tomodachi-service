from abc import ABC, abstractmethod
from uuid import UUID
from app.domain.entities.address_entity import AddressEntity

class AddressRepository(ABC):

    @abstractmethod
    def create(self, address: AddressEntity) -> AddressEntity:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> list[AddressEntity]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> AddressEntity | None:
        pass

    @abstractmethod
    def update(self, address: AddressEntity) -> AddressEntity:
        pass
    
    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass