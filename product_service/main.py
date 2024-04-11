from fastapi import FastAPI
from app.controller.product_routes import router as product_router
from app.controller.category_router import router as category_router

# from fastapi.encoders import jsonable_encoder
from app.core.db import init_db_session
# from app.entity.models import ProductCreate, Product, Category, CategoryCreate
# from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


@app.on_event("startup")
async def startapp():
    await init_db_session()


@app.get("/health_check")
async def health_check():
    return True


app.include_router(product_router, prefix="/api/v1", tags=["Products"])
app.include_router(category_router, prefix="/api/v1", tags=["Category"])


# @app.post("/add_product")
# async def add_product(product_details:ProductCreate):
#     new_product = Product(**jsonable_encoder(product_details))
#     await new_product.insert()
#     return new_product

# @app.post("/add_category")
# async def add_category(category: CategoryCreate):
#     new_category = Category(**jsonable_encoder(category))
#     await Category.insert_one(new_category)
#     return category