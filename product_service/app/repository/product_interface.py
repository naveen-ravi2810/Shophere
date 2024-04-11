from abc import ABC, abstractmethod
from app.entity.models import Product
from app.utils.schema import ProductCreate
from uuid import UUID

class ProductInterface(ABC):
    @abstractmethod
    async def add_product(self, product_details: ProductCreate):
        pass

    @abstractmethod
    async def get_product_by_id(self, product_id: UUID):
        pass

    @abstractmethod
    async def get_product_by_filter(self, filter: dict):
        pass