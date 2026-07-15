from uuid import UUID

from fastapi import APIRouter, Depends, status
from app.application.services.profile.interest_service import InterestService
from app.core.dependencies import get_interest_service
from app.schemas.interest_schema import InterestCreate, InterestUpdate, InterestResponse

router = APIRouter(prefix="/interests")

@router.post("/", response_model=InterestResponse, status_code=status.HTTP_201_CREATED)
def create_interest(
    request: InterestCreate,
    service: InterestService = Depends(get_interest_service),
):
    return service.create(request)

@router.get("/", response_model=list[InterestResponse])
def get_all_interests(
    service: InterestService = Depends(get_interest_service),
):
    return service.get_all()

@router.get("/{interest_id}", response_model=InterestResponse)
def get_interest(
    interest_id: UUID,
    service: InterestService = Depends(get_interest_service),
):
    return service.get_by_id(interest_id)

@router.put("/{interest_id}", response_model=InterestResponse)
def update_interest(
    interest_id: UUID,
    request: InterestUpdate,
    service: InterestService = Depends(get_interest_service),
):
    return service.update(interest_id, request)

@router.delete("/{interest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interest(
    interest_id: UUID,
    service: InterestService = Depends(get_interest_service),
):
    service.delete(interest_id)
