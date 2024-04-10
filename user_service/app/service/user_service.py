from app.repository.user import Users
from app.entity.model import UserCreate, UserLogin
from sqlmodel.ext.asyncio.session import AsyncSession


class UserService:

    def __init__(self):
        self.repository = Users()

    async def create_user(self, new_user: UserCreate, session: AsyncSession) ->  bool:
        return await self.repository.create_user(user_details=new_user, session=session)

    async def login_user(self, login_details: UserLogin, session: AsyncSession) -> dict:
        return await self.repository.login_user(login_details=login_details, session=session)
