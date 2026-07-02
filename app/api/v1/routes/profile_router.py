from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.application.services.me_service import UserService
from app.application.services.profile.profile_service import ProfileService
from app.core.dependencies import get_current_user, get_profile_service, get_me_service
from app.domain.entities.user_entity import UserEntity
from app.schemas.user.profile_schema import ProfileCreate, ProfileUpdate, ProfileResponse
from app.schemas.user.user_schema import UserWithProfileAndAddressResponse

router = APIRouter(prefix="/profiles")

@router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(
    request: ProfileCreate,
    current_user: UserEntity = Depends(get_current_user),
    service: ProfileService = Depends(get_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    user_id = current_user.id
    return service.create(user_id, request)
    
@router.get(
    "/me",
    response_model=UserWithProfileAndAddressResponse,
    response_model_exclude_none=True,
)
def get_profile(
    include_address: bool = Query(
        default=False,
        alias="include_address",
        description="Include user's addresses in the response.",
    ),
    current_user: UserEntity = Depends(get_current_user),
    service: UserService = Depends(get_me_service),
):
    return service.me(current_user.id, include_address)

@router.put("/me", response_model=ProfileResponse)
def update_profile(
    request: ProfileUpdate,
    current_user: UserEntity = Depends(get_current_user),
    service: ProfileService = Depends(get_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    return service.update(current_user.id, request)

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    current_user: UserEntity = Depends(get_current_user),
    service: ProfileService = Depends(get_profile_service),
):
    if current_user.id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    
    service.delete(current_user.id)
