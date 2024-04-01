from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core import security
from app.core.db import get_db_session
from app.models import User

SessionDepends = Annotated[Session, Depends(get_db_session)]


async def get_current_user(
    db: SessionDepends,
    hash: Annotated[str, Header()],
    data_check_string: Annotated[str, Header()],
) -> User:
    """Get current user by tg oauth2 data."""
    if security.verify_user_data(data_check_string, hash):
        for row in data_check_string.split("\n"):
            key, value = row.split("=")
            if key == "id":
                return await crud_user.get_by_telegram_id(db, int(value))
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Данные неверны",
        )


CurrentUserDep = Annotated[User, Depends(get_current_user)]
