from sqlalchemy import create_engine, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session


def create_sqlalchemy_sessionmaker(url: str):  # -> Tuple[AsyncEngine | Engine, AsyncSession | Session]:
    try:
        session_class = AsyncSession
        engine = create_async_engine(
            url,
            poolclass=NullPool,  # AsyncAdaptedQueuePool
        )
    except Exception as e:
        session_class = Session
        engine = create_engine(
            url, connect_args={"check_same_thread": False}
        )
    return async_sessionmaker(engine, expire_on_commit=False, class_=session_class)
