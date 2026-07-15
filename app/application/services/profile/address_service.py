

from uuid import UUID, uuid4

from app.core.exceptions.address_exception import AddressNotFoundException
from app.domain.entities.address_entity import AddressEntity
from app.domain.repositories.address_repository import AddressRepository
from app.schemas.user.address_schema import AddressCreate, AddressUpdate


class AddressService:

    def __init__(self, repository: AddressRepository):
        self.repository = repository

    def create(
        self,
        user_id: UUID,
        request: AddressCreate
    ) -> AddressEntity:

        address = AddressEntity(
            id=uuid4(),
            user_id=user_id,
            province_code=request.province_code,
            province_name=request.province_name,
            regency_code=request.regency_code,
            regency_name=request.regency_name,
            subdistrict_code=request.subdistrict_code,
            subdistrict_name=request.subdistrict_name,
            village_code=request.village_code,
            village_name=request.village_name,
            full_address=request.full_address,
            postal_code=request.postal_code,  
        )

        return self.repository.create(address)

    def get_by_id(self, id: UUID) -> AddressEntity:

        address = self.repository.get_by_id(id)

        if address is None:
            raise AddressNotFoundException()

        return address
    
    def get_by_user_id(self, user_id: UUID) -> list[AddressEntity]:

        addresses = self.repository.get_by_user_id(user_id)

        return addresses

    def update(
        self,
        user_id: UUID,
        request: AddressUpdate
    ) -> AddressEntity:

        address = self.repository.get_by_id(user_id)

        if address is None:
            raise AddressNotFoundException()

        if request.province_code is not None:
            address.province_code = request.province_code
            
        if request.province_name is not None:
            address.province_name = request.province_name

        if request.regency_code is not None:
            address.regency_code = request.regency_code
            
        if request.regency_name is not None:
            address.regency_name = request.regency_name

        if request.subdistrict_code is not None:
            address.subdistrict_code = request.subdistrict_code
            
        if request.subdistrict_name is not None:
            address.subdistrict_name = request.subdistrict_name
            
        if request.village_code is not None:
            address.village_code = request.village_code
            
        if request.village_name is not None:
            address.village_name = request.village_name

        if request.full_address is not None:
            address.full_address = request.full_address
            
        if request.postal_code is not None:
            address.postal_code = request.postal_code

        return self.repository.update(address)

    def delete(self, user_id: UUID) -> None:

        self.repository.delete(user_id)