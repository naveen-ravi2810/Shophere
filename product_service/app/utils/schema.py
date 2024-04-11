from pydantic import Field, BaseModel
from uuid import UUID
from app.entity.models import Category

class CategoryCreate(BaseModel):
    name: str
    description: str


class ProductCreate(BaseModel):
    product_name: str
    product_price: float
    product_discount: float = Field(ge=0, le=100)
    product_quantity: int = Field(ge=0)
    additional_details: dict
    owner_id: UUID
    category_id: UUID
    description: str

