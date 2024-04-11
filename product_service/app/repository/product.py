from app.repository.product_interface import ProductInterface
from app.entity.models import Product
from app.utils.schema import ProductCreate
from uuid import UUID
from app.service.category_service import CategoryService
from fastapi.encoders import jsonable_encoder 
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException, status


category_service = CategoryService()


async def get_category_data(category_id:UUID):
    return await category_service.get_category(category_id=category_id)


class Products(ProductInterface):


    async def add_product(self, product_details:ProductCreate ):
        try:
            category_details = await get_category_data(product_details.category_id)
            new_product = Product(**product_details.dict())   
            await new_product.insert()
            return True
        except DuplicateKeyError as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{new_product.product_name} already exists")
    
    
    async def get_product_by_id(self, product_id: UUID):
        try:
            product = Product.get(id=product_id)
            if product:
                return product
            raise ValueError("No product Found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product_not_found ")


    async def get_product_by_filter(self, filter: dict):
        try:
            product = Product.find_many({Product.additional_details :filter})
            if product:
                return product
            raise ValueError("No product Found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product_not_found ")

