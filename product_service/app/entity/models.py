from beanie import Document, Link, Indexed
from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from typing import Optional
from datetime import datetime


class Category(Document):
    id: UUID = Field(default_factory=uuid4)
    name: Indexed(str, unique=True)
    description: str
    created_at: datetime = Field(default_factory=datetime.now)


class Product(Document):
    product_name: Indexed(str, unique=True)
    product_price: float
    product_discount: float = Field(ge=0, le=100)
    product_quantity: int = Field(ge=0)
    additional_details: dict
    owner_id: UUID
    category_id: UUID
    description: str
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
