import contextlib
from typing import Any, AsyncIterator, Callable

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from shared.core.config import settings


def async_session_factory(
    **engine_params: Any,
) -> tuple[
    Callable[[], AsyncIterator[AsyncSession]],
    Callable[[], contextlib.AbstractAsyncContextManager[AsyncSession]],
    AsyncEngine,
]:
    async_engine_default_params = {"poolclass": NullPool}
    async_engine_default_params.update(engine_params)

    url = str(settings.sqlalachemy_database_uri)
    async_engine = create_async_engine(url, **async_engine_default_params)
    session_factory = async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        future=True,
        expire_on_commit=False,
    )

    async def get_async_session() -> AsyncIterator[AsyncSession]:
        session = session_factory()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.commit()
            await session.close()

    return (
        get_async_session,
        contextlib.asynccontextmanager(get_async_session),
        async_engine,
    )


get_db_session, db_session_manager, db_engine = async_session_factory()
