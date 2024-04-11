from fastapi import APIRouter
from app.utils.schema import ProductCreate
from app.service.product_service import ProductService
from uuid import UUID

router = APIRouter()

product_service = ProductService()

@router.post(path="/add_product")
async def add_product(product_details:ProductCreate):
    return await product_service.add_product(product_details=product_details)
    

@router.get(path="/get_product_by_id")
async def get_product_by_id(product_id:UUID):
    return await product_service.get_product_by_id(product_id=product_id)


# @router.post(path="/get_product_by_filter")
# def get_product_by_filter(filter:dict):
    # try

