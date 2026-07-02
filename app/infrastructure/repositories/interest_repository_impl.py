from app.domain.entities.interest_entity import InterestEntity
from app.domain.repositories.interest_repository import InterestRepository
from sqlalchemy.orm import Session

from app.infrastructure.db.models.interest_model import InterestModel
from app.infrastructure.db.models.profile_interest_model import ProfileInterestModel

class InterestRepositoryImpl(InterestRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, interest: InterestEntity) -> InterestEntity:
        db_interest = InterestModel(
            name=interest.name,
            code=interest.code,
        )
        self.db.add(db_interest)
        self.db.commit()
        self.db.refresh(db_interest)
        
        return InterestEntity(
            id=db_interest.id,
            name=db_interest.name,
            code=db_interest.code,           
        )
        
    def get_by_id(self, id: int) -> InterestEntity | None:
        interest_model = (
            self.db.query(InterestModel)
            .filter(InterestModel.id == id)
            .first()
        )

        if interest_model is None:
            return None

        return InterestEntity(
            id=interest_model.id,
            name=interest_model.name,
            code=interest_model.code,
        )
    
    def get_by_profile_id(self, profile_id: int) -> list[InterestEntity]:
        profile_interests = (
            self.db.query(ProfileInterestModel)
            .filter(ProfileInterestModel.profile_id == profile_id)
            .all()
        )
        
        interest_ids = [pi.interest_id for pi in profile_interests]
        
        if not interest_ids:
            return []
        
        interests = (
            self.db.query(InterestModel)
            .filter(InterestModel.id.in_(interest_ids))
            .all()
        )
        
        return [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code,
            )
            for interest in interests
        ]
    
    def get_all(self) -> list[InterestEntity]:
        interests = self.db.query(InterestModel).all()
        
        return [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code,
            )
            for interest in interests
        ]

    def update(self, interest: InterestEntity) -> InterestEntity:
        interest_model = (
            self.db.query(InterestModel)
            .filter(InterestModel.id == interest.id)
            .first()
        )

        if interest_model is None:
            raise ValueError("InterestEntity not found")

        interest_model.name = interest.name
        interest_model.code = interest.code

        self.db.commit()
        self.db.refresh(interest_model)

        return InterestEntity(
            id=interest_model.id,
            name=interest_model.name,
            code=interest_model.code,
        )

    def delete(self, id: int) -> None:
        interest_model = (
            self.db.query(InterestModel)
            .filter(InterestModel.id == id)
            .first()
        )

        if interest_model is None:
            return

        self.db.delete(interest_model)
        self.db.commit()