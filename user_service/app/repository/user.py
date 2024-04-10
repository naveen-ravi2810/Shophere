from uuid import UUID
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from app.repository.user_interface import UserInterface
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.entity.model import UserCreate, User, UserLogin
from app.core.security import hash_password, check_hash_password, create_access_token, create_refresh_token
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
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


    async def login_user(self, login_details: UserLogin, session:AsyncSession)->dict:
        try:
            statement = select(User).where(User.email == login_details.email)
            user: User = (await session.exec(statement)).one_or_none()
            if not user:
                raise ValueError("No user Found")
            if check_hash_password(login_details.password, user.password):
                access_token = create_access_token(identity=user.user_id, payload={'email':user.email, 'name':user.first_name})
                referesh_token = create_refresh_token(identity=user.user_id, payload={'email':user.email, 'name':user.first_name})
                return {'access_token':access_token, 'refresh_token':referesh_token}
            else:
                raise ValueError("No users found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

    async def user_profile(self, user_id: UUID, session:AsyncSession)->User:
        try:
            pass
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
