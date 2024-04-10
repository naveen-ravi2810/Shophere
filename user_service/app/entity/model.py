from sqlmodel import SQLModel, Field
from uuid import UUID
from uuid_extensions import uuid7
from datetime import datetime


class BaseUUID(SQLModel):
    user_id: UUID = Field(default_factory=uuid7, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now()}
    )


class UserLogin(SQLModel):
    email: str = Field(unique=True, index=True)
    password: str = Field(min_length=8)


class UserCreate(UserLogin):
    phone: str
    first_name: str
    last_name: str


class User(BaseUUID, UserCreate, table=True):
    is_verified: bool = Field(default=False)

class UserProfileInfo(SQLModel):
    phone: str
    first_name: str
    last_name: str
    email: str
    is_verified: bool
    user_id: UUID
    created_at: datetime = Field(default_factory=datetime.now)

