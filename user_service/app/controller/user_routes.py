from fastapi import APIRouter, status, Depends
from app.entity.model import UserCreate
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.db import  get_session
from app.service.user_service import UserService

router = APIRouter()

user_service = UserService()


@router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def create_user(create_details: UserCreate, session:AsyncSession = Depends(get_session)):
    return await user_service.create_user(create_details, session=session)
