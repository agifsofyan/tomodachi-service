from sqlalchemy.orm import Session
from app.domain.entities.address_entity import AddressEntity
from app.domain.repositories.address_repository import AddressRepository
from app.infrastructure.db.models.address_model import AddressModel

class AddressRepositoryImpl(AddressRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, address: AddressEntity) -> AddressEntity:
        db_address = AddressModel(
            user_id=address.user_id,
            province_id=address.province_id,
            province_name=address.province_name,
            regency_id=address.regency_id,
            regency_name=address.regency_name,
            subdistrict_id=address.subdistrict_id,
            subdistrict_name=address.subdistrict_name,
            full_address=address.full_address,
            postal_code=address.postal_code,
        )
        self.db.add(db_address)
        self.db.commit()
        self.db.refresh(db_address)
        
        return AddressEntity(
            id=db_address.id, 
            user_id=db_address.user_id,
            province_id=db_address.province_id,
            province_name=db_address.province_name,
            regency_id=db_address.regency_id,
            regency_name=db_address.regency_name,
            subdistrict_id=db_address.subdistrict_id,
            subdistrict_name=db_address.subdistrict_name,
            full_address=db_address.full_address,
            postal_code=db_address.postal_code,       
        )
        
    def get_by_user_id(self, user_id: int) -> list[AddressEntity]:
        address_model = (
            self.db.query(AddressModel)
            .filter(AddressModel.user_id == user_id)
            .all()
        )
        
        return [
            AddressEntity(
                id=address.id,
                user_id=address.user_id,
                province_id=address.province_id,
                province_name=address.province_name,
                regency_id=address.regency_id,
                regency_name=address.regency_name,
                subdistrict_id=address.subdistrict_id,
                subdistrict_name=address.subdistrict_name,
                full_address=address.full_address,
                postal_code=address.postal_code,   
            )
            for address in address_model
        ]
        
    def get_by_id(self, id: int) -> AddressEntity | None:
        address_model = (
            self.db.query(AddressModel)
            .filter(AddressModel.id == id)
            .first()
        )
        
        if address_model is None:
            return None
        
        return AddressEntity(
            id=address_model.id, 
            user_id=address_model.user_id,
            province_id=address_model.province_id,
            province_name=address_model.province_name,
            regency_id=address_model.regency_id,
            regency_name=address_model.regency_name,
            subdistrict_id=address_model.subdistrict_id,
            subdistrict_name=address_model.subdistrict_name,
            full_address=address_model.full_address,
            postal_code=address_model.postal_code,   
        )

    def update(self, address: AddressEntity) -> AddressEntity:
        address_model = (
            self.db.query(AddressModel)
            .filter(AddressModel.id == address.id)
            .first()
        )

        if address_model is None:
            raise ValueError("AddressEntity not found")

        address_model.province_id = address.province_id
        address_model.regency_id = address.regency_id
        address_model.subdistrict_id = address.subdistrict_id
        address_model.full_address = address.full_address
        address_model.postal_code = address.postal_code

        self.db.commit()
        self.db.refresh(address_model)

        return AddressEntity(
            id=address_model.id, 
            user_id=address_model.user_id,
            province_id=address_model.province_id,
            province_name=address_model.province_name,
            regency_id=address_model.regency_id,
            regency_name=address_model.regency_name,
            subdistrict_id=address_model.subdistrict_id,
            subdistrict_name=address_model.subdistrict_name,
            full_address=address_model.full_address,
            postal_code=address_model.postal_code,   
        )

    def delete(self, user_id: int) -> None:
        profile = (
            self.db.query(AddressModel)
            .filter(AddressModel.user_id == user_id)
            .first()
        )

        if profile is None:
            return

        self.db.delete(profile)
        self.db.commit()