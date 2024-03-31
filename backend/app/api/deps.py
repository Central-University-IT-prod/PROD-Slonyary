import contextlib
from collections.abc import AsyncIterator
from typing import Annotated

from app.core.db import SessionLocal
from app.models import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    db: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]
) -> User:
    """Get current user by JWT token."""
    pass


CurrentUserDep = Annotated[User, Depends(get_current_user)]
