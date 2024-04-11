from fastapi import APIRouter
from uuid import UUID
from app.service.category_service import CategoryService
from app.utils.schema import CategoryCreate


router = APIRouter()

category_service = CategoryService()

@router.get("/get_all_category")
async def get_category():
    return await category_service.get_all_category()
    

@router.get("/get_category")
async def get_category(category_id:UUID):
    return await category_service.get_category(category_id=category_id)


@router.post("/add_category")
async def add_category(category_details: CategoryCreate):
    return await category_service.add_category(category_details=category_details)