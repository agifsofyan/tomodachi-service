from abc import ABC, abstractmethod
from app.domain.entities.address_entity import AddressEntity

class AddressRepository(ABC):

    @abstractmethod
    def create(self, address: AddressEntity) -> AddressEntity:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[AddressEntity]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> AddressEntity | None:
        pass

    @abstractmethod
    def update(self, address: AddressEntity) -> AddressEntity:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass