from app.repository.category import Categories
from app.utils.schema import CategoryCreate
from uuid import UUID


class CategoryService:

    def __init__(self):
        self.repository = Categories()


    async def get_all_category(self):
        return await self.repository.get_all_category()

    
    async def get_category(self, category_id: UUID):
        return await self.repository.get_category(category_id=category_id)


    async def add_category(self, category_details: CategoryCreate):
        return await self.repository.add_category(category_details=category_details)
