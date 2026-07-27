from fastapi import APIRouter, Depends, HTTPException

from app.application.services.auth.login_service import LoginService
from app.application.services.auth.register_service import RegisterService
from app.core.dependencies import get_login_service, get_register_service
from app.schemas.auth_schema import AuthResponse, LoginRequest, RegisterRequest

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=AuthResponse)
def login(request: LoginRequest, service: LoginService = Depends(get_login_service)):
    try:
        return service.execute(request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/register", response_model=AuthResponse)
def register(
    request: RegisterRequest, service: RegisterService = Depends(get_register_service)
):
    try:
        return service.execute(request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
