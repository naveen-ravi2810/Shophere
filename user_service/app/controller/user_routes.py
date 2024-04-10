from fastapi import APIRouter, status, Depends, Response, Cookie
from app.entity.model import UserCreate, UserLogin, UserProfileInfo
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.db import  get_session
from app.service.user_service import UserService
from app.core.security import get_curr_user
from uuid import UUID

router = APIRouter()

user_service = UserService()


@router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def create_user(create_details: UserCreate, session:AsyncSession = Depends(get_session)):
    return await user_service.create_user(create_details, session=session)

@router.post(path="/auth", status_code=status.HTTP_200_OK)
async def login_user(login_details:UserLogin,response:Response, session:AsyncSession = Depends(get_session)):
    tokens = await user_service.login_user(login_details=login_details, session=session)
    response.set_cookie('access_token', tokens['access_token'])
    response.set_cookie('refresh_token', tokens['refresh_token'])
    return True

@router.get(path="/profile", status_code=status.HTTP_200_OK)
async def profile( user_id: UUID = Depends(get_curr_user)):
    return user_id

