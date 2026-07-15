from uuid import UUID, uuid4

from app.core.exceptions.interest_exception import InterestsNotFoundException
from app.domain.entities.interest_entity import InterestEntity
from app.domain.entities.profile_entity import ProfileEntity
from app.domain.repositories.profile_repository import ProfileRepository
from app.domain.repositories.interest_repository import InterestRepository
from app.core.exceptions.profile_exception import ProfileAlreadyExistsException, ProfileNotFoundException
from app.schemas.user.profile_schema import ProfileCreate, ProfileUpdate


class ProfileService:

    def __init__(self, repository: ProfileRepository, interestRepository: InterestRepository):
        self.repository = repository
        self.interestRepository = interestRepository

    def interest_validate(self, ids: list[UUID]) -> list[InterestEntity]:
        interests = self.interestRepository.get_by_ids(ids)

        found_ids = {interest.id for interest in interests}
        invalid_ids = list(set(ids) - found_ids)

        if invalid_ids:
            raise InterestsNotFoundException

        return interests

    def create(
        self,
        user_id: UUID,
        request: ProfileCreate
    ) -> ProfileEntity:

        existing = self.repository.get_by_user_id(user_id)

        if existing is not None:
            raise ProfileAlreadyExistsException()

        profile = ProfileEntity(
            id=uuid4(),
            user_id=user_id,
            gender=request.gender,
            birth_date=request.birth_date,
            hobbies=request.hobbies,
            phone_numbers=request.phone_numbers,
        )
        
        self.interest_validate(request.interests)

        return self.repository.create(profile, interest_ids=request.interests)

    def get_by_user_id(self, user_id: UUID) -> ProfileEntity:

        profile = self.repository.get_by_user_id(user_id)

        if profile is None:
            raise ProfileNotFoundException()

        return profile

    def update(
        self,
        user_id: UUID,
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

    def delete(self, user_id: UUID) -> None:

        self.repository.delete(user_id)