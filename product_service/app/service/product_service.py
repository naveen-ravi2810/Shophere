from app.repository.product import Products
from app.utils.schema import ProductCreate
from uuid import UUID
class ProductService:

    def __init__(self):
        self.repository = Products()

    async def add_product(self, product_details: ProductCreate):
        return await self.repository.add_product(product_details=product_details)

    async def get_product_by_id(self, product_id:UUID):
        return await self.repository.get_product_by_id(product_id=product_id)

    async def get_product_by_filter(self, filter: dict):
        return await self.repository.get_product_by_filter(filter=filter)