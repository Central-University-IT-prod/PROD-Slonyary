import contextlib
from collections.abc import AsyncIterator
from typing import Annotated

from app.core.db import SessionLocal
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session


async def get_async_session() -> AsyncIterator[AsyncSession]:
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.commit()
        await session.close()


SessionDep = Annotated[Session, Depends(get_async_session)]
