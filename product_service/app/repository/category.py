from app.repository.category_interface import CategoryInterface
from uuid import UUID
from fastapi import HTTPException, status
from app.utils.schema import CategoryCreate
from app.entity.models import Category
from pymongo.errors import DuplicateKeyError

class Categories(CategoryInterface):


    async def get_all_category(self):
        try:
            return await Category.find_all().to_list()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No category found")


    async def get_category(self, category_id: UUID):
        try:
            category = await Category.get(document_id=category_id)
            if category:
                return category
            raise ValueError("No Category found")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    async def add_category(self, category_details: CategoryCreate):
        try:
            new_category = Category(**category_details.dict())
            await new_category.insert()
            return True
        except DuplicateKeyError as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{category_details.name} already exists")