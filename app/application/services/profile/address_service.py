

from app.core.exceptions.address_exception import AddressNotFoundException
from app.domain.entities.address_entity import AddressEntity
from app.domain.repositories.address_repository import AddressRepository
from app.schemas.user.address_schema import AddressCreate, AddressUpdate


class AddressService:

    def __init__(self, repository: AddressRepository):
        self.repository = repository

    def create(
        self,
        user_id: int,
        request: AddressCreate
    ) -> AddressEntity:

        address = AddressEntity(
            id=None,
            user_id=user_id,
            province_id=request.province_id,
            province_name=request.province_name,
            regency_id=request.regency_id,
            regency_name=request.regency_name,
            subdistrict_id=request.subdistrict_id,
            subdistrict_name=request.subdistrict_name,
            full_address=request.full_address,
            postal_code=request.postal_code,  
        )

        return self.repository.create(address)

    def get_by_id(self, id: int) -> AddressEntity:

        address = self.repository.get_by_id(id)

        if address is None:
            raise AddressNotFoundException()

        return address
    
    def get_by_user_id(self, user_id: int) -> list[AddressEntity]:

        addresses = self.repository.get_by_user_id(user_id)

        return addresses

    def update(
        self,
        user_id: int,
        request: AddressUpdate
    ) -> AddressEntity:

        address = self.repository.get_by_id(user_id)

        if address is None:
            raise AddressNotFoundException()

        if request.province_id is not None:
            address.province_id = request.province_id
            
        if request.province_name is not None:
            address.province_name = request.province_name

        if request.regency_id is not None:
            address.regency_id = request.regency_id
            
        if request.regency_name is not None:
            address.regency_name = request.regency_name

        if request.subdistrict_id is not None:
            address.subdistrict_id = request.subdistrict_id
            
        if request.subdistrict_name is not None:
            address.subdistrict_name = request.subdistrict_name

        if request.full_address is not None:
            address.full_address = request.full_address
            
        if request.postal_code is not None:
            address.postal_code = request.postal_code

        return self.repository.update(address)

    def delete(self, user_id: int) -> None:

        self.repository.delete(user_id)