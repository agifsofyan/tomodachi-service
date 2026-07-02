from sqlalchemy.orm import Session
from app.domain.entities.interest_entity import InterestEntity
from app.domain.repositories.profile_interest_repository import ProfileInterestRepository
from app.infrastructure.db.models.profile_interest_model import ProfileInterestModel
from app.infrastructure.db.models.interest_model import InterestModel


class ProfileInterestRepositoryImpl(ProfileInterestRepository):
    def __init__(self, db: Session):
        self.db = db

    def add_interests_to_profile(self, profile_id: int, interest_ids: list[int]) -> None:
        for interest_id in interest_ids:
            existing = (
                self.db.query(ProfileInterestModel)
                .filter(
                    ProfileInterestModel.profile_id == profile_id,
                    ProfileInterestModel.interest_id == interest_id
                )
                .first()
            )
            
            if not existing:
                profile_interest = ProfileInterestModel(
                    profile_id=profile_id,
                    interest_id=interest_id
                )
                self.db.add(profile_interest)
        
        self.db.commit()

    def remove_interests_from_profile(self, profile_id: int, interest_ids: list[int]) -> None:
        self.db.query(ProfileInterestModel).filter(
            ProfileInterestModel.profile_id == profile_id,
            ProfileInterestModel.interest_id.in_(interest_ids)
        ).delete(synchronize_session=False)
        
        self.db.commit()

    def get_profile_interests(self, profile_id: int) -> list[InterestEntity]:
        results = (
            self.db.query(InterestModel)
            .join(ProfileInterestModel, ProfileInterestModel.interest_id == InterestModel.id)
            .filter(ProfileInterestModel.profile_id == profile_id)
            .all()
        )
        
        return [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code
            )
            for interest in results
        ]

    def clear_profile_interests(self, profile_id: int) -> None:
        self.db.query(ProfileInterestModel).filter(
            ProfileInterestModel.profile_id == profile_id
        ).delete(synchronize_session=False)
        
        self.db.commit()
    
    def replace_profile_interests(self, profile_id: int, interest_ids: list[int]) -> None:
        self.clear_profile_interests(profile_id)
        
        if interest_ids:
            self.add_interests_to_profile(profile_id, interest_ids)
