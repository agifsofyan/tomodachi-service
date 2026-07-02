from app.domain.entities.profile_entity import ProfileEntity
from app.domain.repositories.profile_repository import ProfileRepository
from app.core.exceptions.profile_exception import ProfileAlreadyExistsException, ProfileNotFoundException
from app.schemas.user.profile_schema import ProfileCreate, ProfileUpdate


class ProfileService:

    def __init__(self, repository: ProfileRepository):
        self.repository = repository

    def create(
        self,
        user_id: int,
        request: ProfileCreate
    ) -> ProfileEntity:

        existing = self.repository.get_by_user_id(user_id)

        if existing is not None:
            raise ProfileAlreadyExistsException()

        profile = ProfileEntity(
            id=None,
            user_id=user_id,
            gender=request.gender,
            birth_date=request.birth_date,
            hobbies=request.hobbies,
            phone_numbers=request.phone_numbers,
        )

        return self.repository.create(profile, interest_ids=request.interests)

    def get_by_user_id(self, user_id: int) -> ProfileEntity:

        profile = self.repository.get_by_user_id(user_id)

        if profile is None:
            raise ProfileNotFoundException()

        return profile

    def update(
        self,
        user_id: int,
        request: ProfileUpdate
    ) -> ProfileEntity:

        profile = self.repository.get_by_user_id(user_id)

        if profile is None:
            raise ProfileNotFoundException()

        if request.gender is not None:
            profile.gender = request.gender

        if request.birth_date is not None:
            profile.birth_date = request.birth_date

        if request.hobbies is not None:
            profile.hobbies = request.hobbies

        if request.phone_numbers is not None:
            profile.phone_numbers = request.phone_numbers

        return self.repository.update(profile, interest_ids=request.interests)

    def delete(self, user_id: int) -> None:

        self.repository.delete(user_id)