from abc import ABC, abstractmethod
from sqlmodel.ext.asyncio.session import AsyncSession
from app.entity.model import UserCreate


class UserInterface(ABC):
    @abstractmethod
    def create_user(self, user_details: UserCreate, session:AsyncSession) -> bool:
        """
        Used to create a user
        """
        pass
