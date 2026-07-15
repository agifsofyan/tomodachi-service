from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from app.application.services.profile.address_service import AddressService
from app.core.dependencies import get_address_service, get_current_user
from app.domain.entities.user_entity import UserEntity
from app.schemas.user.address_schema import AddressCreate, AddressResponse, AddressUpdate

router = APIRouter(prefix="/addresses")

@router.post("/", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
def create_address(
    request: AddressCreate,
    current_user: UserEntity = Depends(get_current_user),
    service: AddressService = Depends(get_address_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Address not found",
        )
    
    user_id = current_user.id
    return service.create(user_id, request)
    
@router.get("/")
def get_addresses(
    current_user: UserEntity = Depends(get_current_user),
    service: AddressService = Depends(get_address_service),
):
    return service.get_by_user_id(current_user.id)

@router.get("/{id}")
def get_address(
    id: UUID,
    service: AddressService = Depends(get_address_service),
):
    return service.get_by_id(id)

@router.put("/{id}", response_model=AddressResponse)
def update_address(
    id: UUID,
    request: AddressUpdate,
    service: AddressService = Depends(get_address_service),
):
    if id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID is required",
        )
    
    return service.update(id, request)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    id: UUID,
    service: AddressService = Depends(get_address_service),
):
    if id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID is required",
        )
    
    service.delete(id)
