from fastapi import APIRouter
from app.api.v1.routes import auth_router, profile_router, interest_router, address_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth_router.router, tags=["auth"])
api_router.include_router(profile_router.router, tags=["profile"])
api_router.include_router(interest_router.router, tags=["interest"])
api_router.include_router(address_router.router, tags=["address"])