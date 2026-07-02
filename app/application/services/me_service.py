from app.core.exceptions.user_exception import UserNotFoundException
from app.domain.repositories.address_repository import AddressRepository
from app.domain.repositories.profile_repository import ProfileRepository
from app.domain.repositories.user_repository import UserRepository
from app.schemas.user.address_schema import AddressResponse
from app.schemas.user.profile_schema import ProfileResponse
from app.schemas.user.user_schema import UserWithProfileAndAddressResponse


class UserService:

    def __init__(
        self,
        user_repository: UserRepository,
        profile_repository: ProfileRepository,
        address_repository: AddressRepository,
    ):
        self.user_repository = user_repository
        self.profile_repository = profile_repository
        self.address_repository = address_repository

    def me(self, user_id: int, include_address: bool) -> UserWithProfileAndAddressResponse:
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundException()

        profile = self.profile_repository.get_by_user_id(user_id)

        result = UserWithProfileAndAddressResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            profile=(
                ProfileResponse.model_validate(profile)
                if profile
                else None
            ),
        )
        
        if include_address is True:
            addresses = self.address_repository.get_by_user_id(user_id)
            result.address = [
                AddressResponse.model_validate(address)
                for address in addresses
            ]
        
        return result