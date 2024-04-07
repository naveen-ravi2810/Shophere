from app.repository.user import Users
from app.entity.model import UserCreate
from sqlmodel.ext.asyncio.session import AsyncSession


class UserService:

    def __init__(self):
        self.repository = Users()

    async def create_user(self, new_user: UserCreate, session: AsyncSession) ->  bool:
        return await self.repository.create_user(user_details=new_user, session=session)
