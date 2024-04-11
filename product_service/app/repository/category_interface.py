from abc import ABC, abstractmethod
from uuid import UUID
from app.utils.schema import CategoryCreate


class CategoryInterface(ABC):

    @abstractmethod
    async def get_all_category(self):
        pass

    @abstractmethod
    async def get_category(self, category_id: UUID):
        pass

    @abstractmethod
    async def add_category(self, category_details: CategoryCreate):
        pass