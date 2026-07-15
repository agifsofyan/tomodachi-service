from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session
from app.application.services.me_service import UserService
from app.application.services.profile.address_service import AddressService
from app.application.services.region.region_service import RegionService
from app.infrastructure.clients.region.region_service import RegionApiClient
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.address_repository_impl import AddressRepositoryImpl
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.infrastructure.repositories.profile_repository_impl import ProfileRepositoryImpl
from app.infrastructure.repositories.interest_repository_impl import InterestRepositoryImpl
from app.application.services.auth.login_service import LoginService
from app.application.services.auth.register_service import RegisterService
from app.application.services.profile.profile_service import ProfileService
from app.application.services.profile.interest_service import InterestService
from app.application.services.auth.token_service import TokenService
from app.core.security import auth_schema, decode_token

def get_user_repository( 
    db: Session = Depends(get_db), 
) -> UserRepositoryImpl: 
    return UserRepositoryImpl(db)

def get_token_service() -> TokenService: 
    return TokenService()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_schema),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    
    try:
        payload = decode_token(token)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token not valid",
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token not valid",
        )

    repository = UserRepositoryImpl(db)
    user = repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user

def get_login_service( 
    repository: UserRepositoryImpl = Depends(get_user_repository),
    token_service: TokenService = Depends(get_token_service), 
) -> LoginService: 
    return LoginService( 
        repository=repository, 
        token_service=token_service
    )
    
def get_register_service( 
    repository: UserRepositoryImpl = Depends(get_user_repository),
    token_service: TokenService = Depends(get_token_service), 
) -> RegisterService: 
    return RegisterService( 
        repository=repository,
        token_service=token_service
    )
    
def get_profile_service(
    db: Session = Depends(get_db), 
) -> ProfileService:
    repository = ProfileRepositoryImpl(db)
    interestRepository = InterestRepositoryImpl(db)
    return ProfileService(repository, interestRepository)

def get_interest_service(
    db: Session = Depends(get_db),
) -> InterestService:
    repository = InterestRepositoryImpl(db)
    return InterestService(repository)

def get_address_service(
    db: Session = Depends(get_db), 
) -> AddressService:
    repository = AddressRepositoryImpl(db)
    return AddressService(repository)

def get_me_service(
    db: Session = Depends(get_db),
) -> UserService:
    user_repository = UserRepositoryImpl(db)
    profile_repository = ProfileRepositoryImpl(db)
    address_repository = AddressRepositoryImpl(db)

    return UserService(
        user_repository=user_repository,
        profile_repository=profile_repository,
        address_repository=address_repository,
    )
    
def get_region_service():
    client = RegionApiClient()
    return RegionService(client)