from app.domain.entities.interest_entity import InterestEntity
from app.domain.entities.profile_entity import ProfileEntity
from app.domain.repositories.profile_repository import ProfileRepository
from app.infrastructure.db.models.profile_model import ProfileModel
from app.infrastructure.db.models.profile_interest_model import ProfileInterestModel
from sqlalchemy.orm import Session, joinedload

class ProfileRepositoryImpl(ProfileRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, profile: ProfileEntity, interest_ids: list[int] | None = None) -> ProfileEntity:
        db_profile = ProfileModel(
            gender=profile.gender,
            user_id=profile.user_id,
            birth_date=profile.birth_date,
            hobbies=profile.hobbies,
            phone_numbers=profile.phone_numbers,
        )
        self.db.add(db_profile)
        self.db.commit()
        self.db.refresh(db_profile)
        
        if interest_ids:
            for interest_id in interest_ids:
                profile_interest = ProfileInterestModel(
                    profile_id=db_profile.id,
                    interest_id=interest_id
                )
                
                self.db.add(profile_interest)
                self.db.commit()
                self.db.refresh(db_profile)
                
        interests = [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code
            )
            for interest in db_profile.interests
        ]
        
        return ProfileEntity(
            id=db_profile.id, 
            gender=db_profile.gender,
            user_id=db_profile.user_id,
            birth_date=db_profile.birth_date,
            hobbies=db_profile.hobbies,
            phone_numbers=db_profile.phone_numbers,
            interests=interests               
        )
        
    def get_by_user_id(self, user_id: int) -> ProfileEntity | None:
        profile_model = (
            self.db.query(ProfileModel)
            .options(joinedload(ProfileModel.interests))
            .filter(ProfileModel.user_id == user_id)
            .first()
        )
        if profile_model is None:
            return None
        # Convert interests to InterestEntity entities
        interests = [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code
            )
            for interest in profile_model.interests
        ]
        return ProfileEntity(
            id=profile_model.id,
            user_id=profile_model.user_id,
            gender=profile_model.gender,
            birth_date=profile_model.birth_date,
            hobbies=profile_model.hobbies,
            phone_numbers=profile_model.phone_numbers,
            interests=interests  # ← ADD THIS
    )

    def update(self, profile: ProfileEntity, interest_ids: list[int] | None = None) -> ProfileEntity:
        profile_model = (
            self.db.query(ProfileModel)
            .filter(ProfileModel.id == profile.id)
            .first()
        )

        if profile_model is None:
            raise ValueError("ProfileEntity not found")

        profile_model.gender = profile.gender
        profile_model.birth_date = profile.birth_date
        profile_model.hobbies = profile.hobbies
        profile_model.phone_numbers = profile.phone_numbers

        self.db.commit()
        
        if interest_ids is not None:
            self.db.query(ProfileInterestModel).filter(
                ProfileInterestModel.profile_id == profile.id
            ).delete(synchronize_session=False)
            
            for interest_id in interest_ids:
                profile_interest = ProfileInterestModel(
                    profile_id=profile.id,
                    interest_id=interest_id
                )
                self.db.add(profile_interest)
                self.db.commit()
        
        self.db.refresh(profile_model)
        
        interests = [
            InterestEntity(
                id=interest.id,
                name=interest.name,
                code=interest.code
            )
            for interest in profile_model.interests
        ]

        return ProfileEntity(
            id=profile_model.id,
            user_id=profile_model.user_id,
            gender=profile_model.gender,
            birth_date=profile_model.birth_date,
            hobbies=profile_model.hobbies,
            phone_numbers=profile_model.phone_numbers,
            interests=interests
        )

    def delete(self, user_id: int) -> None:
        profile = (
            self.db.query(ProfileModel)
            .filter(ProfileModel.user_id == user_id)
            .first()
        )

        if profile is None:
            return

        self.db.delete(profile)
        self.db.commit()