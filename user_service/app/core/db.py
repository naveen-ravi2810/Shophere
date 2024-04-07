from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.settings import db_uri

engine: AsyncEngine = create_async_engine(db_uri.DB_URI)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False,
)


async def get_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session
