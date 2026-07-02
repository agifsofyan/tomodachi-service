from app.domain.entities.user_entity import UserEntity
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.db.models.user_model import UserModel
from sqlalchemy.orm import Session

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, user: UserEntity) -> UserEntity:
        db_user = UserModel(name=user.name, email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserEntity(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)

    def get_by_id(self, user_id: int) -> UserEntity | None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            return UserEntity(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)
        return None

    def get_by_email(self, email: str) -> UserEntity | None:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if db_user:
            return UserEntity(id=db_user.id, name=db_user.name, email=db_user.email, password=db_user.password)
        return None