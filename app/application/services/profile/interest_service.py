from uuid import UUID, uuid4

from app.core.exceptions.interest_exception import InterestAlreadyExistsException, InterestNotFoundException
from app.domain.entities.interest_entity import InterestEntity
from app.domain.repositories.interest_repository import InterestRepository
from app.schemas.interest_schema import InterestCreate, InterestUpdate


class InterestService:

    def __init__(self, repository: InterestRepository):
        self.repository = repository

    def create(self, request: InterestCreate) -> InterestEntity:
        existing = self.repository.get_all()
        
        for interest in existing:
            if interest.code == request.code:
                raise InterestAlreadyExistsException()

        interest = InterestEntity(
            id=uuid4(),
            name=request.name,
            code=request.code,
        )

        return self.repository.create(interest)

    def get_all(self) -> list[InterestEntity]:
        return self.repository.get_all()

    def get_by_id(self, id: UUID) -> InterestEntity:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        return interest

    def update(self, id: UUID, request: InterestUpdate) -> InterestEntity:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        if request.name is not None:
            interest.name = request.name

        if request.code is not None:
            interest.code = request.code

        return self.repository.update(interest)

    def delete(self, id: UUID) -> None:
        interest = self.repository.get_by_id(id)

        if interest is None:
            raise InterestNotFoundException()

        self.repository.delete(id)
