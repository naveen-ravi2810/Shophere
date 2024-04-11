from motor.motor_asyncio import AsyncIOMotorClient
from app.entity.models import Product, Category
from beanie import Document, Indexed, init_beanie



client: AsyncIOMotorClient = AsyncIOMotorClient("mongodb://localhost:27017")


async def init_db_session() -> AsyncIOMotorClient:  # type: ignore
    await init_beanie(database=client.product_service, document_models=[Product, Category])

