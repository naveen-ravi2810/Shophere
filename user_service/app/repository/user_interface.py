from uuid import UUID
from abc import ABC, abstractmethod
from sqlmodel.ext.asyncio.session import AsyncSession
from app.entity.model import UserCreate, UserLogin, User



class UserInterface(ABC):
    @abstractmethod
    async def create_user(self, user_details: UserCreate, session:AsyncSession) -> bool:
        """
        Used to create a user
        """
        pass

    @abstractmethod
    async def login_user(self, login_details: UserLogin, session:AsyncSession) -> dict:
        """
        Used to login a user
        """

    @abstractmethod
    async def user_profile(self, user_id: UUID, session:AsyncSession) -> User:
        """
        Return the user details
        """
        pass
