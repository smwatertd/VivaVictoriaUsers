from models import User

from repositories.base import UserRepository

from schemas import CreateUserSchema

from sqlalchemy.orm import Session


class SQLAlchemyUserRepository(UserRepository):
    def is_user_exists(self, session: Session, **kwargs: dict) -> bool:
        return session.query(User).filter_by(**kwargs).first() is not None

    def create_user(self, session: Session, user: CreateUserSchema) -> None:
        session.add(User(**user.model_dump()))
