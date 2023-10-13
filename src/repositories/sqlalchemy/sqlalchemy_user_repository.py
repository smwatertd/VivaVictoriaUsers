from models import User

from repositories.base import UserRepository

from schemas import CreateUserSchema

from sqlalchemy.orm import Session


class SQLAlchemyUserRepository(UserRepository):
    def create_user(self, session: Session, user: CreateUserSchema) -> None:
        session.add(User(**user.model_dump()))
