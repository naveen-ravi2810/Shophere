from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from app.repository.user_interface import UserInterface
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.entity.model import UserCreate, User
from app.core.security import hash_password
from app.utils.messages import EMAIL_ALREADY_EXISTED


class Users(UserInterface):

    async def create_user(self, user_details: UserCreate, session: AsyncSession) -> bool:
        try:
            encoded_details = jsonable_encoder(user_details)
            new_user = User(**encoded_details)
            new_user.password = hash_password(user_details.password)
            session.add(new_user)
            await session.commit()
            return True
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_226_IM_USED, detail=EMAIL_ALREADY_EXISTED)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_226_IM_USED, detail=str(e))
